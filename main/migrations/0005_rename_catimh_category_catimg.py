# Generated by Django 4.2.3 on 2023-07-06 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_eidted_alter_product_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='catimh',
            new_name='catimg',
        ),
    ]
