# Generated by Django 4.2 on 2024-07-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_review_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(default='Review Title...', max_length=100),
        ),
    ]