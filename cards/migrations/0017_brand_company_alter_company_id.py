# Generated by Django 4.1.3 on 2022-12-02 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0016_remove_brand_company_remove_brand_somethintelse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cards.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
