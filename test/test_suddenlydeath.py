#!/usr/bin/env python

import sys
import unittest

sys.path.append('./../lib/freak')

from suddenlydeath import *

class SuddenlyDeathTests(unittest.TestCase):
    def test_sudden_death(self):
        result = sudden_death("突然の死")
        self.assertEqual(result,
                "＿人人人人人＿\n＞ 突然の死 ＜\n￣^Y^Y^Y^Y^￣")
