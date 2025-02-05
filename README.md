**프로젝트 구조**
/slack-bot-project
│── arxiv_api.py            # arXiv API 연동 모듈
│── database.py             # SQLite 데이터베이스 관리
│── slack_bot.py            # Slack 메시지 전송 기능
│── fetch_papers.py         # 논문을 가져와서 Slack으로 보내는 코드
│── server.py               # 주기적으로 실행하는 서버 코드
│── config.json             # 설정 파일 (API 사용 여부, Slack 토큰, 채널 설정 등)
│── requirements.txt        # 필요한 패키지 목록
