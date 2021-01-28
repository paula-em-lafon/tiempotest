# Generated by Django 3.1.5 on 2021-01-28 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CfdiModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('issuer_name', models.CharField(max_length=100)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('issuer_rfc', models.CharField(max_length=13)),
                ('cfdi_xml', models.TextField()),
                ('total_ammount', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
