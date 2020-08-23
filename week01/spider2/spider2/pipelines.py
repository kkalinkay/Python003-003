# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd
import os

class Spider2Pipeline:
    def process_item(self, item, spider):
        title=item['title']
        type=item['type']
        movie_date=item['movie_date']
        movie_info={"电影名称":[title],"影片类型":[type],"上映日期":[movie_date]}
        #movie_info=[title,type,movie_date]
        data=pd.DataFrame(movie_info)
        # print(data)
        # print(os.path.getsize('./movie.csv'))
        if os.path.getsize('./movie.csv') > 0:
            data.to_csv('./movie.csv',mode='a+',encoding='utf-8',index=False,header=False)
        else:
            data.to_csv('./movie.csv', mode='a+', encoding='utf-8', index=False, header=True)
        return item
