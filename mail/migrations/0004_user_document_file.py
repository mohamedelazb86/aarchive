# Generated by Django 4.2 on 2024-10-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_user_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_document',
            name='file',
            field=models.FileField(default='', upload_to='files_user'),
            preserve_default=False,
        ),
    ]
