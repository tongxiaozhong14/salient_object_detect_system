# Generated by Django 2.2 on 2019-04-27 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190427_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]