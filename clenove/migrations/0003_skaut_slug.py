# Generated by Django 4.0.3 on 2022-05-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clenove', '0002_alter_skaut_options_alter_skaut_jmeno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skaut',
            name='slug',
            field=models.SlugField(default='nic'),
            preserve_default=False,
        ),
    ]
