

def doe_iets(s, n=1):
    """Mijn functie
    
    >>> doe_iets('abc', 3)
    'abcabcabc'

    >>> doe_iets('a', 20)
    'aaaaaaaaaaaaaaaaaaaa'

    >>> doe_iets('xxxx')
    'xxxx'

    """
    return s * n


import unittest
class TestMyFunction(unittest.TestCase):

    def test1(self):
        actual = doe_iets('abc', 3)
        expected = 'abcabcabc'
        self.assertEqual(actual, expected)

    def test2(self):
        actual = doe_iets('a', 20)
        expected = 'aaaaaaaaaaaaaaaaaaaa'
        self.assertEqual(actual, expected)

    def test3(self):
        actual = doe_iets('xxxx')
        expected = 'xxxx'
        self.assertEqual(actual, expected)



# -------------------------------------------

if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)

    unittest.main()

# print(doe_iets('abc', 3))
# print(doe_iets('a', 20))
# print(doe_iets('xxxx'))

# actual = doe_iets('abc', 3)
# expected = 'abcabcabc'
# assert actual == expected, f'Test Failed: {actual} is not equal to {expected}'