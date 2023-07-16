# Generated by Django 3.2.5 on 2022-02-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('parameters', models.JSONField()),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['id', 'name'],
            },
        ),
    ]
