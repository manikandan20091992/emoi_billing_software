# Generated by Django 5.0.1 on 2024-07-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emoi_app', '0002_alter_superadminregister_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superadminregister',
            name='datetime',
            field=models.TextField(blank=True, null=True),
        ),
    ]
