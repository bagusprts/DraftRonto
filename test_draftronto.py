# test_draftronto.py
"""
Tests for DraftRonto module.
"""

import unittest
from draftronto import DraftRonto

class TestDraftRonto(unittest.TestCase):
    """Test cases for DraftRonto class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftRonto()
        self.assertIsInstance(instance, DraftRonto)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftRonto()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
