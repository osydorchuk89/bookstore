# Generated by Django 5.0.7 on 2024-08-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='books.author'),
        ),
    ]
