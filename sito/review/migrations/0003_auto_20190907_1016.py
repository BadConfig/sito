# Generated by Django 2.2.4 on 2019-09-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20190906_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='program',
            field=models.FileField(upload_to='programs/%Y/%m/%d/'),
        ),
    ]