# Generated by Django 3.2.25 on 2024-05-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20240512_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='product_videos/'),
        ),
    ]
