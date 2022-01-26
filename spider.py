from datetime import date, timedelta
from crawler import crawler
from category import categorylist
from pathlib import Path
import config
import pandas as pd
import re


def spider(start_point, end_point):
    print("Beginning to crawl...", end="\n")
    # get date
    today = date.today()
    yesterday = today - timedelta(1)
    today = today.strftime("%b-%d-%Y")
    yesterday = yesterday.strftime("%b-%d-%Y")
    # basis seeting
    p = config.p
    regex = config.regex
    baseurl = config.baseurl
    url_diff_list = []
    # Get list of categories to crawl
    category_list = categorylist(baseurl)
    # iteration
    for i in range(start_point, end_point):
        price_list, url_list = crawler(6, category_list[i])
        # stripping categories
        category_name = re.sub(regex, '', category_list[i])
        url_list = [j for j in dict.fromkeys(url_list).keys()]
        url_df = pd.DataFrame(url_list, columns=["URL"])
        # print(category_name)
        url_df.to_csv(Path(p, f'{category_name}' + '_' + f'{today}.csv'), index=False, sep="\t")
        try:
            url_df_previous = pd.read_csv(Path(p, f'{category_name}' + '_' + f'{yesterday}.csv'), sep="\t")
            url_diff = pd.concat([url_df, url_df_previous]).drop_duplicates(keep=False)
            # print(url_diff)
            url_diff_list += url_diff["URL"].values.tolist()
            print("Updating file..." + category_name )
        except Exception as e:
            print("File from yesterday doesn't exist, creating files...")
    print("Finished today's crawling, going to sleep...")
    url_diff_df = pd.DataFrame(url_diff_list, columns=["URL"])
    url_diff_df.to_csv(Path(p, "difference_" + f'{today}.csv'), index=False, sep="\t")
