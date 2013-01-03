#!/usr/bin/env python
# Copyright 2012 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import unittest
import awscli.clidriver


class TestGetQueueAttributes(unittest.TestCase):

    def setUp(self):
        self.driver = awscli.clidriver.CLIDriver()
        self.prefix = 'aws sqs get-queue-attributes'
        self.queue_url = 'https://queue.amazonaws.com/4444/testcli'

    def test_no_attr(self):
        cmdline = self.prefix + ' --queue-url %s' % self.queue_url
        result = {'QueueUrl': 'https://queue.amazonaws.com/4444/testcli'}
        params = self.driver.test(cmdline)
        self.assertEqual(params, result)

    def test_all(self):
        cmdline = self.prefix + ' --queue-url %s' % self.queue_url
        cmdline += ' --attribute-names All'
        result = {'QueueUrl': 'https://queue.amazonaws.com/4444/testcli',
                  'AttributeName.1': 'All'}
        params = self.driver.test(cmdline)
        self.assertEqual(params, result)

    def test_one(self):
        cmdline = self.prefix + ' --queue-url %s' % self.queue_url
        cmdline += ' --attribute-names VisibilityTimeout'
        result = {'QueueUrl': 'https://queue.amazonaws.com/4444/testcli',
                  'AttributeName.1': 'VisibilityTimeout'}
        params = self.driver.test(cmdline)
        self.assertEqual(params, result)

    def test_two(self):
        cmdline = self.prefix + ' --queue-url %s' % self.queue_url
        cmdline += ' --attribute-names VisibilityTimeout QueueArn'
        result = {'QueueUrl': 'https://queue.amazonaws.com/4444/testcli',
                  'AttributeName.1': 'VisibilityTimeout',
                  'AttributeName.2': 'QueueArn'}
        params = self.driver.test(cmdline)
        self.assertEqual(params, result)


if __name__ == "__main__":
    unittest.main()
