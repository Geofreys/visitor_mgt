# Generated by Django 3.0.6 on 2020-05-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ID_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=20)),
                ('residence', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=30)),
            ],
        ),
    ]