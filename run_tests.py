"""
Discover and run tests
To test:
    python run_tests.py
"""
import unittest

if __name__ == "__main__":
    tests = unittest.defaultTestLoader.discover('tests', pattern='*_test.py')
    unittest.TextTestRunner().run(tests)

