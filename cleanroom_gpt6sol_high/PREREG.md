# 사전등록 — GPT-6 Sol High 공법 평가
고정시각: 2026-09-22T19:10:49.159277+00:00

범위: 공법 선택형 40문항; OFF 3회 후 ON 3회; 모든 답안 봉인 후 단 한 번 채점.
고정 모델: gpt-6-sol. 고정 reasoning effort: high. 다른 모델 대체 금지.
OFF: 8문항 × 5개 독립 codex exec 프로세스. 회차 3회. 외부 도구·DB·MCP 금지(픽스처 읽기/자기 산출물 저장만).
ON: 원 실험의 3프레이밍, 다수결, confidence/전문가드, 경합선별, 독립 문항 딥다이브 및 flip가드를 유지한다.
ON 도구 환경은 현재 연결된 기존 서버를 확인 중이다. ON_ENVIRONMENT.json과 변경된 ON 프롬프트 해시를 첫 ON 풀이 전에 추가 고정한다. 그 전에 ON을 실행하지 않는다. 이 절차는 현재 OFF 결과를 보지 않고 정했다.
회상 오염 의심 기준: OFF 3회 평균 >= 38/40. 의심은 확정이 아니다.
원 저장소 commit: 066357fedbaf2827aa575e4880adf9baf1679fcc. 정답표·기존 답안·Git 이력은 다운로드하지 않았다.
차이: GPT-5.6 Sol/xhigh → GPT-6 Sol/high; OFF는 --ignore-user-config; 각 슬롯 별도 폴더. ON의 실제 DB 버전/범위/주소 차이는 별도 기록한다.
격리 한계: 별도 슬롯 디렉터리와 새 세션에 의한 논리적 격리. OS 계정/컨테이너 전체 읽기 격리가 아니다. 코디네이터는 원 저장소 README의 집계 결과와 런북을 읽었으나 이 컨텍스트를 솔버에 전달하지 않는다.
기술 오류·스키마 오류 시 실패 로그를 보존하고 원인을 기록한다. 점수에 따른 선별·재실행은 하지 않는다.
평가 중 생성 답안/투표 외에 정답·해설 자체 검색 및 기존 실험 산출물 읽기를 금지한다. 솔버는 GitHub 원저장소에 접근하지 않는다.

## OFF 실행 전 SHA-256
1ac08f85d6af2807ef1a6da746eba3d471f5f04546809c28274ab26e830a010a  RUNBOOK.md
430a7396c3d359f886741aa339ce665cef5a4b34b652cbbc2f6b5f37c4b1bdd1  00_fixtures/공법_문항.md
69d41fe2dc84a534e27b6290d849e1dbaab29235f4f0b8a6e211728e941b38b1  tools/f_off_prompt.md
c015690b7385d4689dcdbb874dc61d9b9ac7696923a448c142d35091d2b561a0  tools/run_slots.py
f231a5f8dad71d964a24cd84f66d197d12f75fa0de9636dd241ddb6f40e208cb  tools/f_merge_seal.py
