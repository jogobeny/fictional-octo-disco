import json
import time

import scrapy


class SrealitySpider(scrapy.Spider):
    name = "sreality"

    custom_settings = {
        "ROBOTSTXT_OBEY": False
    }

    def start_requests(self):
        number_of_properties = 500
        current_timestamp_in_milliseconds = time.time_ns()/1_000_000
        urls = [
            "https://www.sreality.cz/api/cs/v2/estates" \
                "?category_main_cb=1" \
                "&category_type_cb=1" \
                f"&per_page={number_of_properties}" \
                f"&tms={current_timestamp_in_milliseconds}"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        for flat in data["_embedded"]["estates"]:
            name = flat["name"]
            images = flat["_links"]["images"]
            image_url = images[0]["href"] if len(images) != 0 else ""

            yield {"name": name, "image_url": image_url}
