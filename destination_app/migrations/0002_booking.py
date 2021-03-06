# Generated by Django 3.1.1 on 2020-10-20 18:12

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('destination_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='0', max_length=50)),
                ('email', models.EmailField(default='0', max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='0', max_length=128, region=None)),
                ('country', django_countries.fields.CountryField(db_index=True, default='0', max_length=2)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('destination', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='destination_app.destination')),
            ],
        ),
    ]
