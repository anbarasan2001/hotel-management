# Generated by Django 4.2.7 on 2023-12-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0002_addroom_modeltable'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking_modelTable',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('rid', models.CharField(max_length=50)),
                ('uid', models.CharField(max_length=50)),
                ('status', models.CharField(default='booking', max_length=50)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]