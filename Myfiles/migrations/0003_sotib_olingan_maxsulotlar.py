# Generated by Django 4.0 on 2021-12-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myfiles', '0002_new_alter_product_rasm2_alter_product_rasm3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sotib_olingan_maxsulotlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
                ('narxi', models.IntegerField()),
                ('miqdori', models.IntegerField()),
                ('mijoz_username', models.CharField(max_length=20)),
                ('mijoz_id', models.IntegerField()),
            ],
        ),
    ]
