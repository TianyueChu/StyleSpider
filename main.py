import schedule
import time
import sys
import config
import spider


def main():
    start = config.start
    end = config.end
    spider.spider(start, end)


if __name__ == "__main__":
    main()

# schedule.every().day.at(config.time).do(spider, start, end)

# while True:
#   schedule.run_pending()
#    time.sleep(1)
