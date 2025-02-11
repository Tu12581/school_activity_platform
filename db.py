

import xml.etree.ElementTree as ET
import pymysql
from pymysql import Error

class Database:
    def __init__(self, config_file="connections.ncx"):
        try:
            # 解析 XML 配置文件
            tree = ET.parse(config_file)
            root = tree.getroot()

            # 提取连接参数
            connection = root.find('Connection')
            host = connection.get('Host')
            port = connection.get('Port', '3306')  # 默认为 3306
            user = connection.get('UserName')
            password = "xhr629185."  # 密码

            # 使用 pymysql 连接到 MySQL 数据库
            self.conn = pymysql.connect(
                host=host,
                port=int(port),
                database="sys",  # 数据库名
                user=user,
                password=password,
                cursorclass=pymysql.cursors.DictCursor  # 可选，使用字典游标返回数据
            )
            self.cursor = self.conn.cursor()
            print("成功连接到数据库")
        except Error as e:
            print(f"数据库连接失败: {e}")
        except ET.ParseError:
            print(f"解析 {config_file} 文件时出错")
        except FileNotFoundError:
            print(f"配置文件 {config_file} 未找到")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except Error as e:
            print(f"执行查询时出错: {e}")

    def fetch_all(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Error as e:
            print(f"获取数据时出错: {e}")
            return []

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


