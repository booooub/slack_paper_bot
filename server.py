import schedule
import time
from fetch_papers import fetch_and_send_papers


# 1시간마다 논문 가져오기
schedule.every(1).hours.do(fetch_and_send_papers)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
