# Generated by Django 4.0.8 on 2022-11-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_cmshome_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmshome',
            name='schema_id',
            field=models.CharField(max_length=255, null=True, verbose_name='Schema ID'),
        ),
    ]
