# Generated by Django 4.2.3 on 2023-07-11 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=None, max_length=255)),
                ('Quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('Cost', models.IntegerField(blank=True, default='0', null=True)),
                ('Orderdttm', models.DateTimeField(auto_now_add=True)),
                ('Is_received', models.BooleanField(default=False)),
                ('Is_cancel', models.BooleanField(default=False)),
                ('Item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Inventory.inventory')),
            ],
            options={
                'db_table': 'Orders',
            },
        ),
    ]