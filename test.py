import unittest
import script

class TestGame(unittest.TestCase):
    
    def testRightGuess(self):
        result = script.game(5, 5)
        self.assertTrue(result)

    def testWrongGuess(self):
        result = script.game(0, 5)
        self.assertFalse(result)

    def testWrongNumber(self):
        result = script.game(11, 5)
        self.assertFalse(result)

    def testWrongType(self):
        result = script.game('11', 5)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()