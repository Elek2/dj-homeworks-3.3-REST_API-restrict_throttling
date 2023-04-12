# Generated by Django 4.2 on 2023-04-12 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0004_alter_favorites_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='advertisement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='f', to='advert.advertisement'),
        ),
    ]