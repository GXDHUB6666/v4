import unittest
if __name__ == '__main__':

    suite = unittest.TestLoader().discover('./scripts',pattern='test*.py')
    unittest.TextTestRunner().run(suite)