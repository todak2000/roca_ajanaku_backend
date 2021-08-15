from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class JoinUs(models.Model):
    class Meta:
        db_table = "Prospective Employees"
    name = models.CharField(max_length=30,verbose_name="Name",blank=True)
    email = models.EmailField(max_length=90, verbose_name="Email", blank=True)
    phone = models.CharField(max_length=15, verbose_name="Telephone number",blank=True)
    document = models.FileField(upload_to='documents/')
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone} - {self.document}"

class Quidroo(models.Model):
    class Meta:
        db_table = "Prospective Users Data"
    name = models.CharField(max_length=100,verbose_name="Name",blank=True)
    email = models.EmailField(max_length=100, verbose_name="Email", blank=True)
    phone = models.CharField(max_length=15, verbose_name="Telephone number",blank=True)
    company = models.CharField(max_length=2000, verbose_name="Company",blank=True)

    type_business = models.CharField(max_length=2000, verbose_name="Type of Business",blank=True)
    address = models.CharField(max_length=2000, verbose_name="Company Address",blank=True)
    confirm_female_cofounder = models.CharField(max_length=15, verbose_name="Is there atleast one female cofounder/owner",blank=True)

    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone} - {self.company} - {self.type_business} - {self.address} - {self.confirm_female_cofounder}"