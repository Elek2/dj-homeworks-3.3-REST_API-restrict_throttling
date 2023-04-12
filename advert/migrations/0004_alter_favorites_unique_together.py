# Generated by Django 4.2 on 2023-04-11 22:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advert', '0003_favorites'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorites',
            unique_together={('user', 'advertisement')},
        ),
    ]