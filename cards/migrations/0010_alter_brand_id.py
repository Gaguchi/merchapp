# Generated by Django 4.1.3 on 2022-12-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0009_alter_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
