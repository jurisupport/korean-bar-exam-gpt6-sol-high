# 사전등록 보정2 — 연결 중단 후 SSE 전송으로 재개

작성시각: 2026-09-24T02:27:58.711356+00:00

도구 사용1회차 첫5묶음에서 스트림 연결단절·재접속대기가 장시간 반복되었고, 교재검색 터널도 끊겼다. 5묶음 모두 최종완료턴과 답안파일이 없음을 확인한 뒤 해당 호출만 종료했다. 미사용1회차70문항 봉인은 유지한다. 중단시도로그·메타데이터는 각 attempt_01 및 meta/network_interruption.json에 보존한다.

기본통신의 무내용 READY 점검도 응답시간초과였다. 같은 공식 ChatGPT Codex 엔드포인트·동일계정·동일 gpt-6-sol/high를 사용하는 SSE 전송(사용자지정 제공자 식별자 exam-openai-sse) 점검이 정상완료했다. 후속 호출에는 SSE를 고정한다. API주소는 https://chatgpt.com/backend-api/codex 이고 외부 제3자 제공자는 사용하지 않는다.

모델·추론강도·문제·풀이프롬프트·허용검색자료·출력스키마는 변경하지 않는다. 기술적 중단된5묶음은 정오정보 없이 동일풀이조건으로 처음부터 재실행한다. 모델 실행의 통신방식 차이는 최종보고에 명시한다.

참조: https://learn.chatgpt.com/docs/config-file/config-reference (사용자지정 제공자 및 supports_websockets).
