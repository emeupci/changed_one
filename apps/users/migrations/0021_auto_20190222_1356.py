# Generated by Django 2.1.7 on 2019-02-22 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Country'),
        ),
    ]
