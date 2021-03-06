# -*- coding: utf-8 -*-

import os.path
import unittest
from picard import util

import __builtin__
# ensure _() is defined
if '_' not in __builtin__.__dict__:
    __builtin__.__dict__['_'] = lambda a: a


class ReplaceWin32IncompatTest(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(util.replace_win32_incompat("c:\\test\\te\"st/2"),
                             "c_\\test\\te_st/2")
        self.assertEqual(util.replace_win32_incompat("A\"*:<>?|b"),
                             "A_______b")

    def test_incorrect(self):
        self.assertNotEqual(util.replace_win32_incompat("c:\\test\\te\"st2"),
                             "c:\\test\\te\"st2")


class SanitizeDateTest(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(util.sanitize_date("2006--"), "2006")
        self.assertEqual(util.sanitize_date("2006--02"), "2006")
        self.assertEqual(util.sanitize_date("2006   "), "2006")
        self.assertEqual(util.sanitize_date("2006 02"), "")
        self.assertEqual(util.sanitize_date("2006.02"), "")
        self.assertEqual(util.sanitize_date("2006-02"), "2006-02")

    def test_incorrect(self):
        self.assertNotEqual(util.sanitize_date("2006--02"), "2006-02")
        self.assertNotEqual(util.sanitize_date("2006.03.02"), "2006-03-02")


class TranslateArtistTest(unittest.TestCase):

    def test_latin(self):
        self.assertEqual(u"Jean Michel Jarre", util.translate_from_sortname(u"Jean Michel Jarre", u"Jarre, Jean Michel"))
        self.assertNotEqual(u"Jarre, Jean Michel", util.translate_from_sortname(u"Jean Michel Jarre", u"Jarre, Jean Michel"))

    def test_kanji(self):
        self.assertEqual(u"Tetsuya Komuro", util.translate_from_sortname(u"小室哲哉", u"Komuro, Tetsuya"))
        self.assertNotEqual(u"Komuro, Tetsuya", util.translate_from_sortname(u"小室哲哉", u"Komuro, Tetsuya"))
        self.assertNotEqual(u"小室哲哉", util.translate_from_sortname(u"小室哲哉", u"Komuro, Tetsuya"))

    def test_kanji2(self):
        self.assertEqual(u"Ayumi Hamasaki & Keiko", util.translate_from_sortname(u"浜崎あゆみ & KEIKO", u"Hamasaki, Ayumi & Keiko"))
        self.assertNotEqual(u"浜崎あゆみ & KEIKO", util.translate_from_sortname(u"浜崎あゆみ & KEIKO", u"Hamasaki, Ayumi & Keiko"))
        self.assertNotEqual(u"Hamasaki, Ayumi & Keiko", util.translate_from_sortname(u"浜崎あゆみ & KEIKO", u"Hamasaki, Ayumi & Keiko"))

    def test_cyrillic(self):
        self.assertEqual(U"Pyotr Ilyich Tchaikovsky", util.translate_from_sortname(u"Пётр Ильич Чайковский", u"Tchaikovsky, Pyotr Ilyich"))
        self.assertNotEqual(u"Tchaikovsky, Pyotr Ilyich", util.translate_from_sortname(u"Пётр Ильич Чайковский", u"Tchaikovsky, Pyotr Ilyich"))
        self.assertNotEqual(u"Пётр Ильич Чайковский", util.translate_from_sortname(u"Пётр Ильич Чайковский", u"Tchaikovsky, Pyotr Ilyich"))


class FormatTimeTest(unittest.TestCase):

    def test(self):
        self.assertEqual("?:??", util.format_time(0))
        self.assertEqual("3:00", util.format_time(179750))
        self.assertEqual("3:00", util.format_time(179500))
        self.assertEqual("2:59", util.format_time(179499))


class HiddenPathTest(unittest.TestCase):

    def test(self):
        self.assertEqual(util.is_hidden_path('/a/.b/c.mp3'), True)
        self.assertEqual(util.is_hidden_path('/a/b/c.mp3'), False)
        self.assertEqual(util.is_hidden_path('/a/.b/.c.mp3'), True)
        self.assertEqual(util.is_hidden_path('/a/b/.c.mp3'), True)
        self.assertEqual(util.is_hidden_path('c.mp3'), False)
        self.assertEqual(util.is_hidden_path('.c.mp3'), True)
        self.assertEqual(util.is_hidden_path('/a/./c.mp3'), False)
        self.assertEqual(util.is_hidden_path('/a/./.c.mp3'), True)
        self.assertEqual(util.is_hidden_path('/a/../c.mp3'), False)
        self.assertEqual(util.is_hidden_path('/a/../.c.mp3'), True)


class TagsTest(unittest.TestCase):

    def test_display_tag_name(self):
        dtn = util.tags.display_tag_name
        self.assertEqual(dtn('tag'), 'tag')
        self.assertEqual(dtn('tag:desc'), 'tag [desc]')
        self.assertEqual(dtn('tag:'), 'tag')
        self.assertEqual(dtn('originalyear'), 'Original Year')
        self.assertEqual(dtn('originalyear:desc'), 'Original Year [desc]')
        self.assertEqual(dtn('~length'), 'Length')
        self.assertEqual(dtn('~lengthx'), '~lengthx')
        self.assertEqual(dtn(''), '')


class LinearCombinationTest(unittest.TestCase):

    def test_0(self):
        parts = []
        self.assertRaises(ZeroDivisionError, util.linear_combination_of_weights, parts)

    def test_1(self):
        parts = [(1.0, 1), (1.0, 1), (1.0, 1)]
        self.assertEqual(util.linear_combination_of_weights(parts), 1.0)

    def test_2(self):
        parts = [(0.0, 1), (0.0, 0), (1.0, 0)]
        self.assertEqual(util.linear_combination_of_weights(parts), 0.0)

    def test_3(self):
        parts = [(0.0, 1), (1.0, 1)]
        self.assertEqual(util.linear_combination_of_weights(parts), 0.5)

    def test_4(self):
        parts = [(0.5, 4), (1.0, 1)]
        self.assertEqual(util.linear_combination_of_weights(parts), 0.6)

    def test_5(self):
        parts = [(0.95, 100), (0.05, 399), (0.0, 1), (1.0, 0)]
        self.assertEqual(util.linear_combination_of_weights(parts), 0.2299)

    def test_6(self):
        parts = [(-0.5, 4)]
        self.assertRaises(ValueError, util.linear_combination_of_weights, parts)

    def test_7(self):
        parts = [(0.5, -4)]
        self.assertRaises(ValueError, util.linear_combination_of_weights, parts)

    def test_8(self):
        parts = [(1.5, 4)]
        self.assertRaises(ValueError, util.linear_combination_of_weights, parts)

    def test_9(self):
        parts = ((1.5, 4))
        self.assertRaises(TypeError, util.linear_combination_of_weights, parts)
