#!/usr/bin/env python
import logging
from listenstore.cli import Command


class KafkaToCassandra(Command):
    desc = "Print listens fetched from kafka"

    def __init__(self):
        super(KafkaToCassandra, self).__init__()
        self.log = logging.getLogger(__name__)

    def run(self):
        self.kafkaConsumer.start_listens(self.listenStore)


if __name__ == '__main__':
    KafkaToCassandra().start()
