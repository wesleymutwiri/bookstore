from django.test import TestCase
from django.urls import resolve
from django.template.loader import render_to_string
from bookworm.views import home_page
from .models import Book

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_template(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		expected_html = render_to_string('bookstore/home.html')
		self.assertTemplateUsed(response, 'bookstore/home.html')

class BookwormModelTest(TestCase):
	def test_saving_and_retrieving_book_titles(self):
		first_book= Book()
		first_book.title = 'The first (ever) book'
		first_book.save()
		second_book = Book()
		second_book.title = 'Second Book here'
		second_book.save()
		saved_books = Book.objects.all()
		self.assertEqual(saved_books.count(),2)
		first_saved_book = saved_books[0]
		second_saved_book = saved_books[1]
		self.assertEqual(first_saved_book.title, 'The first (ever) book')
		self.assertEqual(second_saved_book.title, 'Second Book here') 

	# def test_saving_and_adding