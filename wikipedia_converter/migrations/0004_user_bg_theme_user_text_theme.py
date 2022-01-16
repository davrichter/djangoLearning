# Generated by Django 4.0 on 2022-01-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikipedia_converter', '0003_rename_borrower_fullarticle_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bg_theme',
            field=models.CharField(default='light', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='text_theme',
            field=models.CharField(default='dark', max_length=5),
            preserve_default=False,
        ),
    ]