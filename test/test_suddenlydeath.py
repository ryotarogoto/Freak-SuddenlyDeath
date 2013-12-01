#!/usr/bin/env python

import sys, os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../lib/freak')

from suddenlydeath import *

class SuddenlyDeathTests(unittest.TestCase):
    def test_sudden_death(self):
        result = sudden_death("突然の死")
        self.assertEqual(result,
                "＿人人人人人＿\n＞ 突然の死 ＜\n￣^Y^Y^Y^Y^￣")
