# Generated by Django 2.0.2 on 2018-02-28 13:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180221_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandingCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, help_text='Standing charge price per call', max_digits=12)),
            ],
        ),
        migrations.AlterField(
            model_name='callrecord',
            name='destination',
            field=models.CharField(help_text='The subscriber phone number that originated the call', max_length=11, null=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(message="Phone number must be entered in the format: 'AAXXXXXXXXX'. Where AA is the area code and XXXXXXXXX is the phone number.", regex='^\\d{10,11}$')]),
        ),
        migrations.AlterField(
            model_name='callrecord',
            name='source',
            field=models.CharField(help_text='The subscriber phone number that originated the call', max_length=11, null=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(message="Phone number must be entered in the format: 'AAXXXXXXXXX'. Where AA is the area code and XXXXXXXXX is the phone number.", regex='^\\d{10,11}$')]),
        ),
    ]
