# Generated by Django 4.2 on 2024-10-20 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=120)),
                ('project', models.CharField(max_length=120)),
                ('item', models.CharField(max_length=120)),
                ('notes', models.TextField(max_length=1500)),
                ('archive_code', models.CharField(blank=True, max_length=70, null=True)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractor_sector', to='settings.sector')),
            ],
        ),
    ]
