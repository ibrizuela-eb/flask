import os

import pymysql


def get_connection():
    return pymysql.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'admin'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        db=os.getenv('MYSQL_DATABASE', 'test_db'),
        port=int(os.getenv('MYSQL_PORT', 3306)),
    )
