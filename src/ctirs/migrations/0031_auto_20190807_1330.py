# Generated by Django 1.11.22 on 2019-08-07 04:30


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctirs', '0030_auto_20190605_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='snsconfig',
            name='phantom_auth_token',
            field=models.TextField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='snsconfig',
            name='phantom_host',
            field=models.TextField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='snsconfig',
            name='phantom_playbook_name',
            field=models.TextField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='snsconfig',
            name='phantom_source_name',
            field=models.TextField(default=b'local', max_length=128),
        ),
    ]
