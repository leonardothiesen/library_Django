# Generated by Django 4.2.7 on 2023-11-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_ads', '0003_remove_books_id_alter_books_cod_alter_books_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cover',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
