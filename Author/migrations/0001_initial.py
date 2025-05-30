# Generated by Django 5.1.6 on 2025-02-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('authorid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('bio', models.TextField()),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
