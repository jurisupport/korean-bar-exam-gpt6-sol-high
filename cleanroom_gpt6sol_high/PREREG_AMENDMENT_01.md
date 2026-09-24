# 기술 정정 01 — 법령 도구 초기화 대기
2026-09-22T19:29:43.046107+00:00

초기 ON F1/V1 5슬롯 중 3슬롯이 법령 MCP를 도구 목록에서 찾지 못했다고 보고했다. 다른 2슬롯에서는 실제 MCP 조회가 성공했다.
Codex optional MCP catalog grace가 기본 1초라는 공식 문서를 확인했다. 도구 없이 시작하는 것을 막도록 korean_law.required=true 및 startup_timeout_sec=120을 추가한다.
최초 5슬롯 전부를 점수와 무관하게 기술 실패 회차로 격리했다. 로그/부분 산출물을 invalid_attempts/mcp_startup_001에 보존한다. 이를 유효 답안·투표에 사용하지 않는다.
OFF 3개 봉인본, 프롬프트, 모델/effort, 자료 DB, 시험 기준, 경합 조건, 답 변경 가드는 변경하지 않았다. 정답표/점수는 여전히 미열람.
공식 문서: https://learn.chatgpt.com/docs/extend/mcp

## 변경 전 → 후 SHA-256
run_slots.py: f801c98e653e0028e9d83bee93c2b32178d6399918ac7c71a3e8d6eefa09282b -> 865f08cedcf9dec6ab066128ba191f36e5ab5b56fd7014a651fa37c4f4af38b5
run_deepdives.py: 8c27f9991dd67c4efcd7cd71581a0895eb81aef6af7f1f5ae8da8cf62a74dda4 -> f2c32742f4ca09b6028239b23bb9a838672edb76aefcc4fcc27fb3e2c15f5999
