from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_page_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('BookWorm', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('BookWorm', header_text)
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 
			'Enter a book title'
			)
		inputbox.send_keys('Trial book')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		table = self.browser.find_element_by_id('id_book_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Trial book' for row in rows)
		)
		self.fail("Finished the test!")

if __name__ == '__main__':
	unittest.main(warnings='ignore')
