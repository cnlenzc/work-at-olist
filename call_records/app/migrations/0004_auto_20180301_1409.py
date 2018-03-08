# Generated by Django 2.0.2 on 2018-03-01 14:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180228_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price00h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 00h and 00h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price01h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 01h and 01h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price02h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 02h and 02h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price03h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 03h and 03h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price04h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 04h and 04h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price05h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 05h and 05h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price06h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 06h and 06h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price07h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 07h and 07h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price08h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 08h and 08h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price09h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 09h and 09h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price10h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 10h and 10h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price11h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 11h and 11h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price12h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 12h and 12h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price13h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 13h and 13h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price14h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 14h and 14h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price15h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 15h and 15h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price16h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 16h and 16h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price17h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 17h and 17h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price18h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 18h and 18h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price19h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 19h and 19h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price20h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 20h and 20h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price21h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 21h and 21h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price22h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 22h and 22h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('price23h', models.DecimalField(decimal_places=2, help_text='Call charge per minute between 23h and 23h59', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AlterModelOptions(
            name='standingcharge',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='standingcharge',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Standing charge price per call', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]