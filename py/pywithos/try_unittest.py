#!/usr/bin/env python3
from simple_fct2test import *
from try_raise import *

import unittest

class MytestRearrange(unittest.TestCase):

    def test_basic(self):
        testcase1 = "Herve, Yu"
        expected1 = "Yu Herve"
        self.assertEqual(rearrange_name(testcase1),expected1)

    def test_empty(self):
        testcase = ''
        expected = ''
        res = rearrange_name(testcase)
        self.assertEqual(expected,res)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        res = rearrange_name(testcase)
        self.assertEqual(res,expected)

    def test_raise_correct_error(self):
        self.assertRaises(ValueError,validator_user,"newuser",-1)

    def test_remove_digit_emp_input(self):
        self.assertRaises(ValueError,remove_digit,"")

    def test_remove_digit_nstr_input(self):
        self.assertRaises(AssertionError,remove_digit,["we"])


class MytestFile(unittest.TestCase):

    def test_file_start_with(self):
        filename = "bash_test_file.py"
        self.assertTrue(file_start_with(filename,'bash'))

    def test_mk_new_dir(self):
        dirname = "bash"
        newdir = mk_new_dir(dirname,"N")
        self.assertEqual(dirname,newdir)

    def test_read_filein_exception(self):
        self.assertRaises(OSError,full_path_file,"monfichier.txt","in")

    def test_full_path_file_in(self):
        filename = '_testread.txt'
        path = full_path_file(filename,'in')
        expected = '/Users/herveyu/Desktop/hyu/py/filein/_testread.txt'
        self.assertEqual(expected,path)

    def test_full_path_file_out(self):
        filename = '_testwrite.txt'
        path = full_path_file(filename,'out')
        expected = '/Users/herveyu/Desktop/hyu/py/fileout/_testwrite.txt'
        self.assertEqual(expected,path)


class MytestRemoveDigit(unittest.TestCase):

    def test1(self):
        testcase1 = "You are good2go!"
        expected1 = "You are good to go!"
        result = remove_digit(testcase1)
        self.assertEqual(result,expected1)

unittest.main()
