import os

import psycopg2


class SrealityScrapperPipeline:
    def __init__(self, postgres_host, postgres_database, postgres_user, postgres_password):
        self.postgres_host = postgres_host
        self.postgres_database = postgres_database
        self.postgres_user = postgres_user
        self.postgres_password = postgres_password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            postgres_host="postgres_database",
            postgres_database="postgres",
            postgres_user="postgres",
            postgres_password=os.environ["POSTGRES_PASSWORD"]
        )

    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host=self.postgres_host,
            database=self.postgres_database,
            user=self.postgres_user,
            password=self.postgres_password
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO Flat (title, image_url) VALUES (%s, %s)", (item["name"], item["image_url"]))
        self.connection.commit()

        return item
