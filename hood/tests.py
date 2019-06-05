from django.test import TestCase
from .models import Business,Area,Updates




class areaTestClass(TestCase):
  def setUp(self):
      self.nairobi = Area()