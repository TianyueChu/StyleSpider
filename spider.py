from datetime import date, timedelta
from crawler import crawler
from category import category
import pandas as pd
import re


def spider(start_point, end_point):
    # get date
    today = date.today()
    yesterday = today - timedelta(1)
    today = today.strftime("%b-%d-%Y")
    yesterday = yesterday.strftime("%b-%d-%Y")

    # basis seeting
    baseurl = "https://www.zara.com/es/en/woman-new-in-l1180.html?v1=2026572"
    url_diff_list = []
    category_list = category(baseurl)

    # iteration
    for i in range(start_point, end_point):
        price_list, url_list = crawler(6, category_list[i])
        category_name = re.sub('\d', '', category_list[i].replace("https://www.zara.com/es/en/woman-", "").replace("-l",
                                                                                                                   "").replace(
            ".html", ""))
        url_list = [j for j in dict.fromkeys(url_list).keys()]
        url_df = pd.DataFrame(url_list, columns=["URL"])
        # print(category_name)
        url_df.to_csv(f'{category_name}' + '_' + f'{today}.csv', index=False, sep="\t")
        try:
            url_df_previous = pd.read_csv(f'{category_name}' + '_' + f'{yesterday}.csv', sep="\t")
            url_diff = pd.concat([url_df, url_df_previous]).drop_duplicates(keep=False)
            # print(url_diff)
            url_diff_list += url_diff["URL"].values.tolist()
        except:
            print("File from yesterday doesn't exist")

    url_diff_df = pd.DataFrame(url_diff_list, columns=["URL"])
    url_diff_df.to_csv("difference_" + f'{today}.csv', index=False, sep="\t")
