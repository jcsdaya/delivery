from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User,Group

class Rider(models.Model):
        DISTRICT_CHOICES=[
        ('District 1', 'District 1'),
        ('District 2', 'District 2')
        ]
        riderid = models.AutoField (primary_key=True)
        username = models.CharField(max_length = 150)
        name = models.CharField(max_length = 150)
        location=models.CharField(max_length=75,choices=DISTRICT_CHOICES)
        availability=models.BooleanField(default=False, max_length=15,blank=True,null=True)
        contactnum= models.IntegerField(max_length=11)
        password= models.CharField(max_length=100)

        def __str__ (self):
            return self.username        
       
@receiver(post_save, sender=Rider)
def create_user(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.username, password=str(instance.password))

        group_name = 'Rider'
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)



