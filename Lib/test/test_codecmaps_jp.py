#!/usr/bin/env python
#
# test_codecmaps_jp.py
#   Codec mapping tests for Japanese encodings
#
# $CJKCodecs: test_codecmaps_jp.py,v 1.2 2004/01/17 12:47:19 perky Exp $

from test import test_support
from test import test_multibytecodec_support
import unittest

class TestCP932Map(test_multibytecodec_support.TestBase_Mapping,
                   unittest.TestCase):
    encoding = 'cp932'
    mapfilename = 'CP932.TXT'
    mapfileurl = 'http://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/' \
                 'WINDOWS/CP932.TXT'
    supmaps = [
        ('\x80', u'\u0080'),
        ('\xa0', u'\uf8f0'),
        ('\xfd', u'\uf8f1'),
        ('\xfe', u'\uf8f2'),
        ('\xff', u'\uf8f3'),
    ]
    for i in range(0xa1, 0xe0):
        supmaps.append((chr(i), unichr(i+0xfec0)))


class TestEUCJPCOMPATMap(test_multibytecodec_support.TestBase_Mapping,
                         unittest.TestCase):
    encoding = 'euc_jp'
    mapfilename = 'EUC-JP.TXT'
    mapfileurl = 'http://people.freebsd.org/~perky/i18n/EUC-JP.TXT'


class TestSJISCOMPATMap(test_multibytecodec_support.TestBase_Mapping,
                        unittest.TestCase):
    encoding = 'shift_jis'
    mapfilename = 'SHIFTJIS.TXT'
    mapfileurl = 'http://www.unicode.org/Public/MAPPINGS/OBSOLETE' \
                 '/EASTASIA/JIS/SHIFTJIS.TXT'
    pass_enctest = [
        ('\x81_', u'\\'),
    ]
    pass_dectest = [
        ('\\', u'\xa5'),
        ('~', u'\u203e'),
        ('\x81_', u'\\'),
    ]


class TestSJISSTRICTMap(test_multibytecodec_support.TestBase_Mapping,
                        unittest.TestCase):
    encoding = 'shift_jis_strict'
    mapfilename = 'SHIFTJIS.TXT'
    mapfileurl = 'http://www.unicode.org/Public/MAPPINGS/OBSOLETE' \
                 '/EASTASIA/JIS/SHIFTJIS.TXT'


class TestEUCJISX0213Map(test_multibytecodec_support.TestBase_Mapping,
                         unittest.TestCase):
    encoding = 'euc_jisx0213'
    mapfilename = 'EUC-JISX0213.TXT'
    mapfileurl = 'http://people.freebsd.org/~perky/i18n/EUC-JISX0213.TXT'


class TestSJISX0213Map(test_multibytecodec_support.TestBase_Mapping,
                       unittest.TestCase):
    encoding = 'shift_jisx0213'
    mapfilename = 'SHIFT_JISX0213.TXT'
    mapfileurl = 'http://people.freebsd.org/~perky/i18n/SHIFT_JISX0213.TXT'


def test_main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCP932Map))
    suite.addTest(unittest.makeSuite(TestEUCJPCOMPATMap))
    suite.addTest(unittest.makeSuite(TestSJISCOMPATMap))
    if test_multibytecodec_support.__cjkcodecs__:
        suite.addTest(unittest.makeSuite(TestSJISSTRICTMap))
    suite.addTest(unittest.makeSuite(TestEUCJISX0213Map))
    suite.addTest(unittest.makeSuite(TestSJISX0213Map))
    test_support.run_suite(suite)

test_multibytecodec_support.register_skip_expected(TestCP932Map,
    TestEUCJPCOMPATMap, TestSJISCOMPATMap, TestEUCJISX0213Map,
    TestSJISX0213Map)
if __name__ == "__main__":
    test_main()
