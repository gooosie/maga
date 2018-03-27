from maga import Maga

import logging
logging.basicConfig(level=logging.INFO)


class Crawler(Maga):
    async def handler(self, infohash, addr):
        logging.info(infohash)

crawler = Crawler()
crawler.run(port=6881, rate=100)
