from django.db import models
from rider.models import Rider
from django.utils import timezone
from django.core.exceptions import ValidationError

class Dispatch(models.Model):
        STATUS_CHOICES = [
        ('Preparing', 'Preparing'),
        ('On the Way', 'On the Way'),
        ('Delivered', 'Delivered'),
        ]
        PAYMENT_CHOICES = [
        ('Card', 'Card'),
        ('GCASH', 'GCASH'),
        ('COD', 'COD'),
        ]
        dispatchrider = models.ForeignKey (Rider,on_delete=models.CASCADE,null=True,blank=True)
        dispatchid = models.AutoField(primary_key=True)
        status=models.CharField(max_length=20,default='Preparing',choices=STATUS_CHOICES)
        order = models.CharField(max_length=20)
        orderpayment = models.CharField(max_length=20,choices=PAYMENT_CHOICES)
        dropoff=models.CharField(max_length=500)
        pickup=models.CharField(max_length=500)
        deliverydate = models.DateTimeField(default=timezone.now)
        complete = models.BooleanField(default=False)

        def clean(self):
                if self.dispatchrider and not self.dispatchrider.availability:
                        raise ValidationError('Selected rider is not available')



       


