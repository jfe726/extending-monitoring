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


#class RemoteDemoPlugin():
class RemoteDemoPlugin(RemoteBasePlugin):
    def initialize(self, **kwargs):
        self.args = {}

        self.args['id'] = kwargs['config']['id']
        self.args['url'] = kwargs['config']['url']
        self.args['port'] = kwargs['config']['port']
        self.args['debug'] = kwargs['config']['debug']

        print("ID=" + self.args['id'])
        print("URL=" + self.args['url'])
        print("PORT=" + self.args['port'])
        print("DEBUG=" + self.args['debug'])
        print()

        return
    
    def query(self, **kwargs):
        try:
            logger.info("--- Begin execution ---")

            start_time = time.time()

            content = self.query_url(self.args['url'] + ":" + self.args['port'])
            content = json.loads(content)

            print("CONTENT=" + str(content))
            print()

            custom_counter = int(content["counter"])
            custom_random = int(content["random"])

            if self.args['debug'] == "false":
                group = self.topology_builder.create_group(self.args['url'], self.args['url'])

                element = group.create_element(self.args['url'], self.args['url'])

                element.add_endpoint(self.args['url'], int(self.args['port']))

                element.report_property('Time', str(datetime.datetime.now()))

                element.absolute(key="custom_counter", value=custom_counter)
                element.absolute(key="custom_random", value=custom_random)
            else:
                print("CREATE GROUP: " + self.args['url'])
                print("CREATE ELEMENT: " + self.args['url'])
                print("ADD ENDPOINT: " + self.args['url'] + ":" + self.args['port'])
                print("REPORT PROPERTY: " + str(datetime.datetime.now()))
                print("REPORT METRIC: " + str(custom_counter))
                print("REPORT METRIC: " + str(custom_random))
                print()

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

#class Test:
#    @staticmethod
#    def test1():
#        id = "host-1"
#        url = "http://35.233.65.127"
#        port = "8769"
#        debug = "true"
#
#        plugin = RemoteDemoPlugin()
#        plugin.initialize(config={"id": id, "url": url, "port": port, "debug": debug"})
#        plugin.query()
#
#
#if __name__ == "__main__":
#    Test.test1()