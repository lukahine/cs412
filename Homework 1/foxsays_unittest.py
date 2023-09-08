"""
       Name: Kevin Molloy
    
    Purpose: Showcase how to use unittest to verify/test the foxsays
             homework assignment.
"""

import unittest

from io import StringIO
from unittest.mock import patch

from cs412_foxsays_list import main as fox_list_main
from cs412_foxsays_dict import main as fox_dict_main

class TestHW1(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.file_a_ok = False
        cls.file_b_ok = False
        cls.t0_in = """toot woof wa ow ow ow pa blub blub pa toot pa blub pa pa ow pow toot
5
dog goes woof
fish goes blub
elephant goes toot
seal goes ow
horse goes neigh
what does the fox say?"""
        cls.t0_exp = 'what the fox says: wa pa pa pa pa pa pow\nalso heard: elephant dog seal fish\n'
        
        cls.t1_in = """fox makes sounds
0
what does the fox say?"""
        cls.t1_exp = 'what the fox says: fox makes sounds \nalso heard: \n'


    def test_01(self):
        """Check file cs412_foxsays_list does not contain a dictionary"""

        dict_char = False
        with open('cs412_foxsays_list.py') as f:
            if '{' in f.read():
                dict_char = True

        with open('cs412_foxsays_list.py') as f:
            if 'dict()' in f.read():
                dict_char = True

        self.assertEqual(False, dict_char, 
                          'Appears that a dictionary is used in cs412_foxsays_list.py')
        
        # test OK, set status to good/true
        TestHW1.file_a_ok = True

    def test_02(self):
        """Check file cs412_foxsays_dict does contain a dictionary"""

        dict_char = False
        with open('cs412_foxsays_dict.py') as f:
            if '{' in f.read():
                dict_char = True
                
        with open('cs412_foxsays_dict.py') as f:                
            if 'dict()' in f.read():
                dict_char = True

        self.assertEqual(True, dict_char, 
                          'Appears that a dictionary is NOT used in cs412_foxsays_list.py')
        
        # test OK, set status to good                  
        TestHW1.file_b_ok = True

    
    @patch('sys.stdout', new_callable=StringIO)
    def test_03(self, mock_out):
        """Test 1 from write up on cs412_foxsays_list"""
        self.assertEqual(True, TestHW1.file_a_ok, "File cs412_foxsays_list test skipped because of dictionary detected")

        with patch('sys.stdin', new = StringIO(self.t0_in)):
            fox_list_main()
        self.assertEqual(mock_out.getvalue(), self.t0_exp)

    @patch('sys.stdout', new_callable=StringIO)
    def test_04(self, mock_out):
        """Test 2 from write up on cs412_foxsays_list"""
        self.assertEqual(True, TestHW1.file_a_ok, "File cs412_foxsays_list test skipped because of dictionary detected")

        with patch('sys.stdin', new = StringIO(self.t0_in)):
            fox_list_main()
        self.assertEqual(mock_out.getvalue(), self.t0_exp)

    
    @patch('sys.stdout', new_callable=StringIO)
    def test_05(self, mock_out):
        """Test 1 from write up on cs412_foxsays_dict"""
        self.assertEqual(True, TestHW1.file_b_ok,  "File cs412_foxsays_dict test skipped because no dictionary detected")

        with patch('sys.stdin', new = StringIO(self.t0_in)):
            fox_dict_main()
        self.assertEqual(mock_out.getvalue(), self.t0_exp)

    @patch('sys.stdout', new_callable=StringIO)
    def test_06(self, mock_out):
        """Test 2 from write up on cs412_foxsays_dict"""
        self.assertEqual(True, TestHW1.file_b_ok,  "File cs412_foxsays_dict test skipped because no dictionary detected")

        with patch('sys.stdin', new = StringIO(self.t0_in)):
            fox_dict_main()
        self.assertEqual(mock_out.getvalue(), self.t0_exp)
