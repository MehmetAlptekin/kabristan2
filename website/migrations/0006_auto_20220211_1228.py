# Generated by Django 3.1.5 on 2022-02-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_referancebilgi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='referancebilgi',
            options={'verbose_name_plural': 'Referans'},
        ),
        migrations.RenameField(
            model_name='newsletterbilgi',
            old_name='newsletter',
            new_name='name',
        ),
        migrations.AddField(
            model_name='newsletterbilgi',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newsletterbilgi',
            name='phone',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='newsletterbilgi',
            name='surname',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
