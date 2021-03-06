# Generated by Django 2.2.13 on 2021-04-13 00:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JoinUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=90, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Telephone number')),
                ('document', models.FileField(upload_to='documents/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Prospective Employees',
            },
        ),
    ]
