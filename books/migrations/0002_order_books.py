# Generated by Django 5.0.3 on 2024-04-02 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(to='books.book'),
        ),
    ]