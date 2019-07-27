import unittest
import app

class TestApp(unittest.TestCase):
    """
    Unit test for app
    """

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_name(self):
        name = 'Simon'
        rv = self.app.get('/hello/%s' % name)
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(name, rv.data)

if __name__ == '__main__':
    unittest.main()