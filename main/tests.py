from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    #testing admin login untuk soal bonus
    def test_admin_login(self):
        response = Client().get('/admin/login/', {'username': 'dell', 'password': '12345678'})
        self.assertEqual(response.status_code, 200)