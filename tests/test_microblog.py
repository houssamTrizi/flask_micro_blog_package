#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_microblog
----------------------------------

Tests for `microblog` module.
"""

import unittest

import microblog


class TestMicroblog(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(microblog.__version__)

    def tearDown(self):
        pass
