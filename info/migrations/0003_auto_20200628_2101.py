# Generated by Django 3.0.6 on 2020-06-29 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='Filecontent',
            field=models.FileField(blank='', null='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='notice',
            name='imgcontent',
            field=models.ImageField(blank='', null='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='notice',
            name='textcontent',
            field=models.TextField(blank='', null=''),
        ),
    ]
