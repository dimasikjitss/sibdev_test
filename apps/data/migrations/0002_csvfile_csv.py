# Generated by Django 3.1.5 on 2021-01-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfile',
            name='csv',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]