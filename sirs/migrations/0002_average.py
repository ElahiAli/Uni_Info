# Generated by Django 3.2.9 on 2021-12-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AVERAGE',
            fields=[
                ('STNAME', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('STID', models.CharField(max_length=10)),
                ('AVE', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
            ],
        ),
    ]
