# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ProxyspiderPipeline:
    def open_spider(self,spider):
        #连接数据库
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='rootroot',
                               database='test')
        self.conn=conn
        self.cs=conn.cursor()

        self.cs.execute("create table movie(movie_title varchar(100),movie_type varchar(100),movie_data varchar(100))")
        #提前修改本机数据库编码，允许插入中文
        #my.ini文件sql-mode去掉STRICT_TRANS_TABLES

        self.conn.commit()

    def process_item(self, item, spider):
        title=item['title']
        type=item['type']
        date=item['date']
        print(f'insert into movie values(\'{title}\',\'{type}\',\'{date}\');')
        try:
            self.cs.execute(f'insert into movie values(\'{title}\',\'{type}\',\'{date}\');')
            self.conn.commit()
        except Exception as e:
            print(e)
        # value=(title,type,date)
        # print(value)
        # self.cs.executemany('insert into table movie values(%s,%s,%s)', value)
        # self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cs.close()
        self.conn.close()