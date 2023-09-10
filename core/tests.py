from django.test import TestCase

# Create your tests here.


class PostPageTest(TestCase):
    def test_uses_post_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "index.html")
