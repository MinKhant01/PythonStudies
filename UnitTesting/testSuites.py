import unittest

def suite():
    suite = unittest.testSuite()
    suite.addTest(TestClass('test_method'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())