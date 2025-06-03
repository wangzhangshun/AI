# 案例1
from DrissionPage import *
import time,json

import pandas as pd
from datetime import datetime

from DataRecorder import Recorder


def extract_comments(data):
    comments = []

    if 'result' not in data:
       return []
    if 'floors' not in data['result']:
       return []

    # 遍历floors找到commentlist-list楼层
    for floor in data['result']['floors']:
        if floor.get('mId') == 'commentlist-list' and 'data' in floor:
            for item in floor['data']:
                if 'commentInfo' in item:
                    comment = item['commentInfo']

                    # 处理可能缺失的字段
                    after_comment = comment.get('afterComment', {})
                    ware_attr = comment.get('wareAttribute', [{}])[0]

                    # 提取核心信息
                    comments.append({
                        'user': comment['userNickName'],
                        'score': int(comment['commentScore']),
                        'date': comment['commentDate'],
                        'content': comment['commentData'],
                        'after_comment': after_comment.get('content'),
                        'after_days': after_comment.get('timeText', '').replace('购后', '').replace('天追评', ''),
                        'product_spec': ware_attr.get('颜色', ''),
                        'praise_count': int(comment['praiseCnt']),
                        'image_count': len(comment.get('pictureInfoList', [])),
                        'is_video': any(pic.get('mediaType') == '2'
                                        for pic in comment.get('pictureInfoList', [])),
                        'user_level': comment.get('officerLevel', '0'),
                        'repurchase': comment.get('repurchaseInfo', ''),
                        'tags': ', '.join([icon['iconId'] for icon in comment.get('iconList', [])])
                    })

    return pd.DataFrame(comments)



def main():
    # r = Recorder('JD.csv')
    # # 1.实例化参数类
    # co = ChromiumOptions()
    # # co.headless(False)
    # co.auto_port()
    #
    # # 2 实例化浏览器引擎
    # page = ChromiumPage(co)

    page = ChromiumPage(9333)

    url = "https://item.jd.com/100006466663.html"
    page.listen.start('client.action')
    page.get(url)
    if page.ele('@text()=全部评价'):
        page.ele('@text()=全部评价').click(by_js=True)
        # res = page.listen.wait(count=1, timeout=20, fit_count=True)
        # print("data:::",res.response.body)
        while True:
            js = page.listen.wait(count=1,timeout=60,fit_count=True)
            if not js:
                break

            # df = extract_comments(js.response.body)

            df = extract_comments(js.response.body)

            # if null == df || df.size == 0:
            #     break

            # 数据增强：计算评论长度、提取年月日
            df['content_length'] = df['content'].str.len()
            df['comment_date'] = pd.to_datetime(df['date']).dt.date

            # 保存结果
            df.to_csv('jd_comments_processed.csv', index=False, encoding='utf-8-sig')
            print(f"共提取 {len(df)} 条评价，样例：")
            print(df[['user', 'score', 'content_length', 'comment_date']].head(3))
            # for comment in (extract_comments(js.response.body)):
            #     data_dict = {
            #         "用户名": comment.get('userNickName',''),
            #         "用户等级": "",
            #         "评论时间": comment.get('commentDate', ''),
            #         "评论内容": comment.get('commentData', ''),
            #         "评分（星级）": comment.get('commentScore', ''),
            #         "地区": "",
            #     }


if __name__ == '__main__':
    main()
