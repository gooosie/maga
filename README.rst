Maga
====


A DHT crawler framework using asyncio.


Usage
-----
.. code-block:: python

    from maga import Maga
    
    import logging
    logging.basicConfig(level=logging.INFO)
    
    
    class Crawler(Maga):
        async def handler(self, infohash, addr):
            logging.info(addr)
            logging.info(infohash)


    # Or, if you want to have more control

    class Crawler(Maga):
        async def handle_get_peers(self, infohash, addr):
            logging.info(
                "Receive get peers message from DHT {}. Infohash: {}.".format(
                    addr, infohash
                )
            )

        async def handle_announce_peer(self, infohash, addr, peer_addr):
            logging.info(
                "Receive announce peer message from DHT {}. Infohash: {}. Peer address:{}".format(
                    addr, infohash, peer_addr
                )
            )


    crawler = Crawler()
    # Set port to 0 will use a random available port
    # Set rate to 50 will limit processing only about 50 query requests per second
    # and other requests will be dropped.
    # If rate is <= 0, there will be no rate limit.
    crawler.run(port=0, rate=50)


ChangeLog
----------
Version 4.1.1
~~~~~~~~~~~~~~~
+ Add query rate limiter base on queue.
+ Add `name` param to `handle_announce_peer` method.

Version 3.0.0
~~~~~~~~~~~~~~~

+ Add `peer_addr` param to `handle_announce_peer` method.
+ Don't raise NotImplementedError on `handler`

Version 2.0.1
~~~~~~~~~~~~~~~

+ Don't fail when signals are not implemented.( `#3 <https://github.com/whtsky/maga/pull/3>`_ )

Version 2.0.0
~~~~~~~~~~~~~~~

+ Add `handle_get_peers`, `handle_announce_peer` method.
+ Add `addr` param to `handler`