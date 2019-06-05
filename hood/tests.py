from django.test import TestCase
from .models import Business,Area,Updates




class areaTestClass(TestCase):
  def setUp(self):
      self.nairobi = Area(name = 'Nairobi', population = '25')

  def test_instance(self):
    self.asserTrue(isinstance(self.nairobi,Area))

  def test_save_method(self):
      self.nairobi.create_business()
      area = Area.objects.all()
      self.assertTrue(len(editors) > 0 )

  def test_save_method(self):
      self.nairobi.create_business()
      area = Area.objects.all()
      self.assertTrue(len(editors) > 0 )

