# Generated by Django 3.2.7 on 2022-02-23 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_alter_avukatbilgi_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='hizmetlerimiz',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
