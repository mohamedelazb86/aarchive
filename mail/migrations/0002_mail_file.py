# Generated by Django 4.2 on 2024-10-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='file',
            field=models.FileField(default='', upload_to='files_mail'),
            preserve_default=False,
        ),
    ]