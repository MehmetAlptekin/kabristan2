# Generated by Django 3.1.5 on 2022-02-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_blogbilgi_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
