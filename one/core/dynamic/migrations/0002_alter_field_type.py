# Generated by Django 4.0.8 on 2022-11-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='type',
            field=models.CharField(choices=[('CharField', 'Char Field')], default='CharField', max_length=50, verbose_name='Type of Field'),
        ),
    ]
