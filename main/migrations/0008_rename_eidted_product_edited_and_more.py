# Generated by Django 4.2.3 on 2023-07-06 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_product_eidted_alter_product_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='eidted',
            new_name='edited',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='upload',
            new_name='uploaded',
        ),
    ]
