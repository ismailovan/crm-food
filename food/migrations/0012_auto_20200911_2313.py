# Generated by Django 3.1.1 on 2020-09-11 17:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_auto_20200911_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 9, 11, 17, 13, 11, 298572, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Checks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('meals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.mealtoorder')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.order')),
                ('servicefee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.servicepercentage')),
            ],
        ),
    ]
