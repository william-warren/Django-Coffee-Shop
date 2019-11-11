# Generated by Django 2.2.5 on 2019-11-07 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('pre_tax', models.FloatField()),
                ('tax', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Coffee')),
            ],
        ),
    ]