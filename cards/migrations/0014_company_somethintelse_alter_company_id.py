# Generated by Django 4.1.3 on 2022-12-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0013_alter_brand_id_alter_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='somethintelse',
            field=models.CharField(default=11, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]