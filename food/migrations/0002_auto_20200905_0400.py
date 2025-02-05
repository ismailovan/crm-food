# Generated by Django 3.1.1 on 2020-09-04 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealtoorder',
            name='meal',
        ),
        migrations.AddField(
            model_name='mealtoorder',
            name='meal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='food.meal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mealtoorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals_id', to='food.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.table', verbose_name='Table'),
        ),
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Waiter'),
        ),
    ]
