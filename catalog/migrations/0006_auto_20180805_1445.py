# Generated by Django 2.0.7 on 2018-08-05 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180805_1336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('can_view_all_borrowed', 'View all borrowed'))},
        ),
    ]
