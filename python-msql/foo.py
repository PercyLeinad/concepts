import mysql.connector
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    conn = mysql.connector.connect(
        host = os.getenv('HOST'),
        user = os.getenv('USER'),
        password = os.getenv('PASSWORD'),
        database = os.getenv('DATABASE')
    )

    cur = conn.cursor()

    cur.execute("""describe table book""")

    row = cur.fetchone()

    print(row)
    
    cur.close()
    conn.close()

main()


# def process_item(self, item, spider):
#     ## Check to see if text is already in database 
#     self.cur.execute("select * from book where title = %s", (item['title'],))
#     result = self.cur.fetchone()

#     ## If it is in DB, create log message
#     if result:
#         spider.logger.warn("Item already in database: %s" % item['title'])
#     else:
#         ## Define insert statement
#         self.cur.execute(""" insert into book (title, price, rating, image_url) values (%s,%s,%s,%s)""", (
#             item["title"],
#             item["price"],
#             item["rating"],
#             item["image_url"]
#         ))

#         ## Execute insert of data into database
#         self.conn.commit()
#     return item