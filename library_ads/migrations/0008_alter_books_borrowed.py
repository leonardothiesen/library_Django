# Generated by Django 4.2.7 on 2023-12-01 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_ads', '0007_alter_books_borrowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='borrowed',
            field=models.IntegerField(default=0),
        ),
    ]