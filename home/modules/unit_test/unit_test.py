# Make unittest in the
# app.py program

# Import packages
from app import app
import unittest

# Create the class that is
# going to make the UnitTest

class FlaskTextCase(unittest.TestCase):

	# Ensure that Flask
	# was set up correctly

	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/inicio', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# Ensure that the
	# "Calcule address"
	# page loads correctly

	def test_form_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/inicio', content_type='html/text')
		self.assertTrue(b'Calcule the Distance between two poin' in response.data)

	# Ensure that the
	# "Calcule address"
	# form page, requires data

	def test_form_requires(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects=True)
		self.assertIsNotNone(b'You need to write your address first.' 
			in response.data)

if __name__ == '__main__':
	unittest.main()
