# Generated by Django 5.1.1 on 2024-10-17 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xeber',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='homepage.category'),
        ),
    ]
