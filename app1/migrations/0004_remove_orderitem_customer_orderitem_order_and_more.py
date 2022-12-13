# Generated by Django 4.1.3 on 2022-12-12 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='customer',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orders',
            field=models.CharField(max_length=80),
        ),
    ]