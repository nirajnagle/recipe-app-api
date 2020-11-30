from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful."""
        email = 'test@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email = email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    
    def test_new_user_email_normalized(self):
        """ Test the email for new user is normalized."""
        email = 'test@GMAil.COM'
        user = get_user_model().objects.create_user(email,'test123')
        
        self.assertEqual(user.email, email.lower())
    
    
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test1234')
    
    
    def test_create_new_superuser(self):
        """Creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test123@gmail.com', 
            'password'
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)                