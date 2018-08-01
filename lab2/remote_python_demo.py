import sys
import os
import json
import logging
import time
import requests
import datetime
import ruxit.api.exceptions
from ruxit.api.base_plugin import RemoteBasePlugin
from requests.exceptions import ReadTimeout
from urllib.parse import urlparse
from collections import defaultdict, namedtuple

logger = logging.getLogger(__name__)


class RemoteDemoPlugin(RemoteBasePlugin):
    def initialize(self, **kwargs):
        self.args = {}

        self.args['id'] = kwargs['config']['id']
        self.args['url'] = kwargs['config']['url']
        self.args['port'] = kwargs['config']['port']
        self.args['debug'] = kwargs['config']['debug']

        logger.info("ID=" + self.args['id'])
        logger.info("URL=" + self.args['url'])
        logger.info("PORT=" + self.args['port'])
        logger.info("DEBUG=" + self.args['debug'])

        return
    
    def query(self, **kwargs):
        try:
            logger.info("--- Begin execution ---")

            start_time = time.time()

            content = self.query_url(self.args['url'] + ":" + self.args['port'])
            content = json.loads(content)

            logger.info("CONTENT=" + str(content))

            custom_counter = int(content["counter"])
            custom_random = int(content["random"])

            group = self.topology_builder.create_group(self.args['url'], self.args['url'])

            element = group.create_element(self.args['url'], self.args['url'])

            element.add_endpoint(self.args['url'], int(self.args['port']))

            element.report_property('Time', str(datetime.datetime.now()))

            element.absolute(key="custom_counter", value=custom_counter)
            element.absolute(key="custom_random", value=custom_random)

            end_time = time.time()

            logger.info("--- Statistics ---")
            logger.info("--- Execution time: %s seconds ---" % (end_time - start_time))
        except Exception as exc:
            logger.error("Exception: " + str(exc))

        return

    def query_url(self, url):
        logger.info("Querying url: " + url)

        content = None

        max_retries = 2
        retries = 0
        while retries < max_retries:
            retries = retries + 1
            try:
                r = requests.get(url, verify=False, timeout=2)
                content = r.content.decode('UTF-8')

                return content
            except Exception as exc:
                logger.error("Exception: " + str(exc))
                continue

        return content
    
