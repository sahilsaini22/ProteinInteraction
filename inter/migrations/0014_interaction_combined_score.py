# Generated by Django 3.1.5 on 2021-01-12 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inter', '0013_interaction_textmining'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='combined_score',
            field=models.IntegerField(default=0),
        ),
    ]
