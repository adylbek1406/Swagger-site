# Generated by Django 5.0.2 on 2024-03-01 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0005_alter_branch_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='position',
            field=models.CharField(default='Пример позиции', max_length=255),
        ),
    ]