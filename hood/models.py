  
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

    

class Area(models.Model):
    name = models.CharField(max_length=50, blank=True)
    population = models.CharField(max_length=50, blank=True)
    

    

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_neighborhood(self, neigborhood_id):
        self.search_by_id(id=neigborhood_id)

    def update_neighborhood(self):
        self.update_area()

    def update_occupants(self):
        self.update_population()

    def __str__(self):
        return self.name
                                                  
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='media/')
    bio = models.TextField(blank=True)
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Area, null=True, on_delete=models.CASCADE)

    

    def save_user(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.bio

class Business(models.Model):
    business_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(null=False)
    category = models.CharField(max_length = 250,null = True )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, null=True, on_delete=models.CASCADE)

    @classmethod
    def area_businesses(cls,area):
        businesses = Business.objects.filter(area__pk=area)
        return businesses

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(self, business_id):
        self.search_by_id(id=business_id)

    def update_business(self):
        self.update()

    def __str__(self):
        return self.business_name


class Updates(models.Model):
    title = models.CharField(max_length=500, blank=True)
    post = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    posted_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    area = models.ForeignKey(Area,on_delete=models.CASCADE,null=True)


    @classmethod
    def area_updates(cls,area):
        updates = cls.objects.filter(area__pk=area)
        return updates

    def create_update(self):
        self.save()

    def delete_update(self):
        self.delete()

    def update(self):
        self.update()

    def __str__(self):
        return self.title

