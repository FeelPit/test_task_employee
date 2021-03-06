# Generated by Django 3.1.5 on 2022-05-13 11:39

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0010_auto_20200508_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.country')),
            ],
        ),
    ]
