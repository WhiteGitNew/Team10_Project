from django.test import TestCase
from comment.models import Comment

class CommentModelTests(TestCase):
    def test_ensure_comments_text_valid(self):
        """
        Ensure the number of comments is not ""
        """
        cmt = Comment(comment_id=3,comment_text="",count_all_liked=20,article_id=12,comment_user_id=12)
        cmt.save()
        text = cmt.comment_text
        self.assertEqual(((len(text) == 0) or text.isspace()), False)
# Create your tests here.
