# Generated by Django 4.0.3 on 2022-07-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0035_remove_kisidetay_category_delete_detaykategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='kisiDetayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('surname', models.CharField(blank=True, max_length=200, null=True)),
                ('birth_date', models.DateField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, default='profile_pics/default.jpg', upload_to='')),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]