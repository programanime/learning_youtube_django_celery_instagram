# Generated by Django 3.0.7 on 2020-07-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0002_auto_20200728_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
