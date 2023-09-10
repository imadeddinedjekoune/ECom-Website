# Generated by Django 4.2.4 on 2023-08-17 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_0', models.ImageField(upload_to='products/images/list/')),
                ('image_1', models.ImageField(upload_to='products/images/list/')),
                ('image_2', models.ImageField(upload_to='products/images/list/')),
                ('image_3', models.ImageField(upload_to='products/images/list/')),
                ('image_4', models.ImageField(upload_to='products/images/list/')),
                ('image_5', models.ImageField(upload_to='products/images/list/')),
                ('image_6', models.ImageField(blank=True, null=True, upload_to='products/images/list/')),
                ('image_7', models.ImageField(blank=True, null=True, upload_to='products/images/list/')),
                ('image_8', models.ImageField(blank=True, null=True, upload_to='products/images/list/')),
                ('image_9', models.ImageField(blank=True, null=True, upload_to='products/images/list/')),
                ('image_10', models.ImageField(blank=True, null=True, upload_to='products/images/list/')),
                ('new', models.BooleanField(default=False)),
                ('promotion', models.PositiveIntegerField(null=True)),
                ('promotion_prix', models.FloatField(null=True)),
                ('small_description', models.TextField(blank=True)),
                ('desc_specifications', models.TextField(null=True)),
                ('desc_utilisation', models.TextField(null=True)),
                ('desc_etat', models.TextField(null=True)),
                ('desc_livraison', models.TextField(null=True)),
                ('desc_autre', models.TextField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.subcategory')),
            ],
        ),
    ]
