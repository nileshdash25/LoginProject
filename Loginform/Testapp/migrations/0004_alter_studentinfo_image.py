# Generated by Django 4.2.3 on 2023-08-18 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Testapp', '0003_studentinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='image',
            field=models.ImageField(default='', upload_to='C:/Users/Nilesh/Desktop'),
        ),
    ]