from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class JoinUs(models.Model):
    class Meta:
        db_table = "Prospective Employees"
    user_id = models.CharField(max_length=500,unique=True)
    name = models.CharField(max_length=30,verbose_name="Name",blank=True)
    email = models.EmailField(max_length=90, unique=True,verbose_name="Email")
    phone = models.CharField(max_length=15, unique=True, null=True, verbose_name="Telephone number")
    document = models.FileField(upload_to='documents/')
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user_id} - {self.name} - {self.email} - {self.phone} - {self.document}"