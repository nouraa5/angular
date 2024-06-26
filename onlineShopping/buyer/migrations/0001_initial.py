# Generated by Django 5.0.3 on 2024-04-02 21:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=35)),
                ('password', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('zipcode', models.CharField(max_length=200, null=True)),
                ('cardname', models.CharField(max_length=200, null=True)),
                ('cardnumber', models.CharField(max_length=20)),
                ('expdate', models.CharField(max_length=255)),
                ('prod_count', models.IntegerField(blank=True, null=True)),
                ('total_amt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cvv', models.CharField(blank=True, max_length=4, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buyer.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_desc', models.TextField(blank=True, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('product_keywords', models.TextField(blank=True, null=True)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.brands')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('order_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.orders')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField(blank=True, default=0, null=True)),
                ('ip_addr', models.CharField(max_length=45)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.customuser')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.product')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.role'),
        ),
    ]
