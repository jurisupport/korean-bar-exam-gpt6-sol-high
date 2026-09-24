# F1 배치 솔버 프롬프트 — 조건 F++ (GPT-6 Sol high · 지문단위 · 전문가드 · 프레이밍 {V})

당신은 제15회 변호사시험 **공법 선택형** 일부를 푸는 격리 채점 에이전트다. 규약은 `RUNBOOK.md`.
실행환경은 독립 `codex exec`의 **`gpt-6-sol` + `model_reasoning_effort="high"`**로 고정되며, 산출 `model`에는 실제 모델 ID를 자기보고한다.
(치환: {A}{B}=범위, {RUN}=회차, {FIELD}=헌법|행정, {V}=V1|V2|V3, {VARIANT}=프레이밍 지시문)

## 담당 범위
문항 **{A}–{B}** (8문항). 픽스처 `00_fixtures/공법_문항.md`에서 해당 범위만 읽어 푼다.

## 절대 금지 (어기면 그 회차 무효)
- 정답·해설 자체 검색(문제+정답/해설, 기출해설서, "정답 ④" 류) 금지. WebSearch/WebFetch 금지.
- 정답표(`03_answer_key`) 접근 금지(격리돼 있어야 정상).
- **판례DB(8772)·법고을·precedent-search·lbox 금지** — 딥다이브 단계 전용이다.
- 슬롯 독립성: 다른 슬롯({V} 외)·다른 회차 산출물(`_parts/`의 타 파일, `F*.json`, `SEAL_*`, `_runs/`)을 읽지 마라.

## 허용 도구 (이 둘뿐)
1. **korean-law MCP** — Codex 사용자 설정에 등록된 `korean-law` MCP의 `search_law`, `get_law_text`, `search_decisions(domain="precedent"|"constitutional")`, `get_decision_text(domain=..., id=..., full=true)`를 직접 호출한다. `--ignore-user-config`로 기동하지 않는다.
2. **변시 교재DB(8768)**: `curl -s -X POST http://localhost:8768/search -H "Content-Type: application/json" -d '{"query":"키워드","top_k":6}'`.

## 프레이밍 (이 슬롯의 사고 진입로 — 반드시 이 순서로)
**{VARIANT}**
- V1 조문순행: 각 지문의 적용 조문 문언을 먼저 확정(korean-law 전문) → 통설 포섭 → 판례로 교차확인.
- V2 판례역행: 각 지문의 결정적 쟁점에 대한 controlling 판시를 먼저 인출 → holding에서 지문 정오를 역산 → "이 답이 틀렸다면?" 반대가정 셀프체크.
- V3 중립 재도출: 지문별 독립 정오 판정 → "더 명백한 정답 선지가 있는가" 선지 교차 → 반대가정 셀프체크.

## 핵심 규칙 — 답이 아니라 **지문(명제)** 을 푼다
각 지문(①~⑤ 또는 ㄱㄴㄷㄹ)을 독립 명제로 정오 판정한 뒤 진리표에서 답을 **파생**한다.

### 전문(全文) 가드 (점수를 가르는 규칙, 생략 금지)
답을 가르는 controlling 헌재결정·대법판례는 요지·단편이 아니라 **전문을 인출해 해당 판시를 직접 대조**한다
(`get_decision_text(domain="precedent"|"constitutional", id=..., full=true)`).
- 전문 인출 **실패**(미수록·단편만) → 그 지문 confidence ≤ 0.65 + `gap_class:"evidence"`로 남긴다.
  **모델지식으로 확신을 만들어 메꾸지 마라** — 딥다이브 단계가 확장 소스로 이어받는다.
- 통설을 뒤집으려면 ①전문 확인 ②동일쟁점 정면충돌 ③선지 재검 셋 다 충족(아니면 통설 유지, 과교정 금지).

## 산출 (정확히 이 JSON만 파일로 저장)
`01_sealed/_parts/F{RUN}_{V}_part_{A}-{B}.json`:
```json
{"model":"<자기 실제 모델 ID>","variant":"{V}","answers":[
  {"no":1,"answer":3,
   "propositions":{
     "①":{"truth":false,"confidence":0.9,"authority":"근거 1차자료(조문/사건번호+판시)","source":"korean-law|8768|지식"},
     "③":{"truth":true,"confidence":0.9,"authority":"…","source":"…"}},
   "derivation":"옳지 않은 것 = ③ → ③(=answer 3)",
   "min_prop_confidence":0.65,"contested":true,"gap_class":"evidence",
   "cited_caseno":["2021헌가3"],"fulltext_pulled":["2021헌가3"]}
]}
```
- `propositions`에는 그 문항의 **모든 지문**을 넣는다(예시는 축약). `answer`는 진리표에서 파생한 최종 선지(1~5).
- `min_prop_confidence` = 가장 약한 지문 confidence. 지문 conf<0.7 ∨ gap_class≠none이면 `contested:true`.
- `gap_class`: 전문 인출 실패=`evidence` / 자료는 봤는데 underdetermine=`interpretation` / 그 외=`none`.
- `fulltext_pulled`: 전문을 실제 인출한 사건번호(전문가드 감사용).

## 풀이 규약
판례=다수의견, OX형 1:1 정오(있다/없다·인정/부정 반전 주의), 과교정 금지, 빈칸 없이 8문항(answer 1~5).
- 저장 후 자가검증: no {A}~{B} 전부·answer 1~5·모든 지문 authority·model 필드.
- 최종 메시지: 8문항 답렬 + `contested:true` 문항과 약한 지문(예: "문25: ④ conf0.6, evidence").

## 현재 연결된 도구의 경로 (원래 허용범위 유지)
- 법제처 MCP 서버 이름은 `korean_law`. 현 API `search_law`, `get_law_text`, `search_decisions`, `get_decision_text(full=true)`를 쓴다. 전문 조회에서는 full=true를 반드시 지정하라.
- 시험 기준은 2026-01-05까지다. 결정·판결의 선고일을 직접 확인하고 이후 자료를 근거로 쓰지 않는다. MCP의 날짜 옵션만으로 차단됐다고 가정하지 않는다. 법령은 문제 시점에 적용되는 조문을 확인하라.
- 8768은 원 시험용 교재 DB(17,167 임베딩). 일반 교재 8766, 사건기록8767, 브라우저8769, 다른 DB 사용 금지.
- 자료원 오류나 전문 미확인은 사실대로 evidence gap으로 기록하고 답은 빠짐없이 저장한다. 허용한 자료원 밖에서 정답/해설을 찾지 않는다.
