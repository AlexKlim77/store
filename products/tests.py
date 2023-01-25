from django.test import TestCase
from django.urls import reverse


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)
        # print(response)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')
