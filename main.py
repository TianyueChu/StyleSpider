import schedule
import time
from spider import spider

schedule.every().day.at("17:20").do(spider,start_point=3,end_point=17)

while True:
    schedule.run_pending()
    time.sleep(1)