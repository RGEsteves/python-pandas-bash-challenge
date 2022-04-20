# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_average_post(self):
        """Test case for average_post

        Returns the average file size
        """
        data = dict(zfile=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/challenge/average',
            method='POST',
            data=data,
            content_type='application/zip')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_biggest_post(self):
        """Test case for biggest_post

        Returns the biggest file
        """
        data = dict(zfile=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/challenge/biggest',
            method='POST',
            data=data,
            content_type='application/zip')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_histogram_post(self):
        """Test case for histogram_post

        Returns the histogram of file sizes
        """
        data = dict(zfile=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/challenge/histogram',
            method='POST',
            data=data,
            content_type='application/zip')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_smallest_post(self):
        """Test case for smallest_post

        Returns the smallest file
        """
        data = dict(zfile=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/challenge/smallest',
            method='POST',
            data=data,
            content_type='application/zip')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
