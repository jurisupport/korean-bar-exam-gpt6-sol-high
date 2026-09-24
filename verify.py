"""Verify published answer scores, answer seals, file hashes and Markdown links."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    totals = {"off": [0, 0, 0], "on": [0, 0, 0]}
    for folder, label, size in [
        ("cleanroom_gpt6sol_high", "공법", 40),
        ("civil_gpt6sol_high", "민사법", 70),
        ("criminal_gpt6sol_high", "형사법", 40),
    ]:
        base = ROOT / folder
        key = read(base / "03_answer_key" / f"{label}_정답.json")["key"]
        public = label == "공법"
        summary = read(base / ("04_scoring/SUMMARY.json" if public else "SUMMARY.json"))
        assert set(key) == {str(i) for i in range(1, size + 1)}, label
        for mode in ("off", "on"):
            scores = []
            for i in range(1, 4):
                run = (f"Foff{i}" if mode == "off" else f"F{i}") if public else f"{mode}_p{i}"
                path = base / (f"01_sealed/{run}.json" if public else f"runs/{run}/answers.json")
                answers = read(path)["answers"]
                assert len(answers) == size and {a["no"] for a in answers} == set(range(1, size + 1)), run
                assert all(type(a["answer"]) is int and 1 <= a["answer"] <= 5 for a in answers), run
                wrong = sorted(a["no"] for a in answers if a["answer"] != key[str(a["no"])])
                score = size - len(wrong)
                expected = summary["scores"][run] if public else summary["results"][run]["score"]
                expected_wrong = summary["wrong_questions"][run] if public else summary["results"][run]["wrong"]
                assert score == expected and wrong == expected_wrong, run
                if public:
                    seal = (base / f"01_sealed/SEAL_{run}.txt").read_text()
                    assert re.search(rf"{digest(path)}\s+01_sealed/{run}\.json", seal), run
                else:
                    seal = read(path.parent / "SEAL.json")
                    assert seal["files"]["answers.json"] == digest(path), run
                scores.append(score)
                totals[mode][i - 1] += score
            print(f"{label} {mode}: {scores}/{size}")
    manifest = read(ROOT / "PUBLICATION_MANIFEST.json")
    for entry in manifest["files"]:
        assert digest(ROOT / entry["path"]) == entry["published_sha256"], entry["path"]
    for path in ROOT.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if not re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) and not target.startswith("#"):
                assert (path.parent / unquote(target.split("#")[0])).exists(), (path, target)
    assert totals == {"off": [127, 120, 119], "on": [145, 146, 147]}, totals
    print(f"PASS: 18 primary scores/seals, {len(manifest['files'])} published hashes, Markdown links; totals={totals}")


if __name__ == "__main__":
    main()
