
from unittest import TestCase

from ..connectors import fetch_dvf, fetch_dvf_for_city


class ConnectorsTestCase(TestCase):

    def test_fetch_dvf(self):
        data = fetch_dvf('2018', '75', '75119')
        print(data.info())

    def test_fetch_dvf_for_city(self):
        fetch_dvf_for_city('lille')
