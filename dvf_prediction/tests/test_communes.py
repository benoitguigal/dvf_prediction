from unittest import TestCase

from ..communes import get_code_commune


class CommunesTestCase(TestCase):

    def test_get_code_commune(self):
        """ it should return all commune code for a specific city """
        codes = get_code_commune('PARIS')
        expected = ['75103', '75105', '75108', '75110', '75112', '75115',
                    '75118', '75120', '75102', '75104', '75116', '75111',
                    '75116', '75117', '75106', '75113', '75119', '75101',
                    '75107', '75109', '75114']
        for code in expected:
            self.assertIn(code, codes)
