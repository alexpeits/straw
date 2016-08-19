import unittest
import sys

sys.path.append('./')
sys.path.append('../')


tests = unittest.TestLoader().discover('tests')
unittest.TextTestRunner(verbosity=2).run(tests)
