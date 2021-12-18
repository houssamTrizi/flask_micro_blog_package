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

    def test_something_fails(self):
        assert 1/0

    def tearDown(self):
        pass
