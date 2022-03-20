from django.test import TestCase
from theme.models import Article,Artheme
# Create your tests here.

class ArticleMethodTests(TestCase):
    def test_ensure_comments_positive(self):
        """
        Ensure the number of comments for a Article are positive or zero
        """
        art = Article(article_title="testArticle",article_id=2,count_all_commented=-5,article_author_id=12,article_theme_id=12)
        art.save()

        self.assertEqual((art.count_all_commented >=0), True)

class ArthemeMethodTests(TestCase):
    def test_ensure_articlesnum_positive(self):
        """
        Ensure the number of articles for each theme are greater than 0
        """
        theme = Artheme(at_id=1,at_name='python',at_count=-10,at_author_id=12)
        theme.save()
        self.assertEqual((theme.at_count > 0), True)

# class IndexViewTests(TestCase):
#     def test_ensure_theme_created(self):
#         """
#         Ensure new theme created
#         """
#         theme = forms.ArticleThemeForm()

