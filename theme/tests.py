from django.test import TestCase
from theme.models import Article, Artheme

class ArthemeAddMethodTests(TestCase):
    def test_ensure_theme_is_created(self):
        """
        Ensure new theme is created by function
        """
        theme = Artheme.objects.create()


# class ArticleModelTestCase(TestCase):
#     def setUp(self):
#         article  = Article
