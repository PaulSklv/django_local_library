from django.test import TestCase

# Create your tests here.
''' class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)'''


from catalog.models import Author
from catalog.models import Book, Genre, BookInstance, Language

class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Genre.objects.create(name = 'Non-fiction')

    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length,200)

    def test_name_is_name(self):
        genre = Genre.objects.get(id=1)
        expected_object_name = '%s' % (genre.name)
        self.assertEquals(expected_object_name,str(genre))

class LanguageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Language.objects.create(name = 'Non-fiction')

    def test_name_label(self):
        lang = Language.objects.get(id=1)
        field_label = lang._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_name_max_length(self):
        lang = Language.objects.get(id=1)
        max_length = lang._meta.get_field('name').max_length
        self.assertEquals(max_length,200)

    def test_name_is_name(self):
        lang = Language.objects.get(id=1)
        expected_object_name = '%s' % (lang.name)
        self.assertEquals(expected_object_name,str(lang))


class BookModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Book.objects.create(title='Intresting book.')

	def test_title_lable(self):
		book = Book.objects.get(id = 1)
		field_label = book._meta.get_field('title').verbose_name
		self.assertEquals(field_label, 'title')

	def test_title_max_length(self):
		book = Book.objects.get(id = 1)
		max_length = book._meta.get_field('title').max_length
		self.assertEquals(max_length, 200)

	def test_isbn_lable(self):
		book = Book.objects.get(id = 1)
		field_label = book._meta.get_field('isbn').verbose_name
		self.assertEquals(field_label, 'ISBN')

	def test_isbn_max_length(self):
		book = Book.objects.get(id = 1)
		max_length = book._meta.get_field('isbn').max_length
		self.assertEquals(max_length, 13)

	def test_get_absolute_url(self):
		book=Book.objects.get(id=1)
		#This will also fail if the urlconf is not defined.
		self.assertEquals(book.get_absolute_url(),'/catalog/book/1')

class BookInstanceModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		BookInstance.objects.create(imprint = 'Designed by')

	def test_imprint_lable(self):
		bookinst = BookInstance.objects.get(imprint = 'Designed by')
		field_label = bookinst._meta.get_field('imprint').verbose_name
		self.assertEquals(field_label, 'imprint')

	def test_inprint_max_length(self):
		bookinst = BookInstance.objects.get(imprint = 'Designed by')
		max_length = bookinst._meta.get_field('imprint').max_length
		self.assertEquals(max_length, 200)


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label,'died')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name,str(author))

    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/catalog/authors/1')
