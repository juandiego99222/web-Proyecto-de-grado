from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.


#test para saber si a lo que se registra un usuario se crea el perfil
class ProfileTestCase(TestCase):
    def setUp(self):
       User.objects.create_user('test','test@test.com', 'test1234')

    def test_profile_exist(self):
       exists =Profile.objects.filter(user__username='test').exists()
       self.assertEqual(exists,True)



       