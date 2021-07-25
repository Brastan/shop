# Generated by Django 3.2.5 on 2021-07-22 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_tag',
        ),
        migrations.AddField(
            model_name='item',
            name='item_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item', to='shop_list.tag'),
        ),
    ]
