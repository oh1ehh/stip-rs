# Generated by Django 1.10.4 on 2019-02-20 07:46


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctirs', '0017_auto_20190220_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='administraive_code',
            new_name='administrative_code',
        ),
    ]
