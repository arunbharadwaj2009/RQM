# Generated by Django 2.2.7 on 2019-11-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potholes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jsonfile', models.FileField(upload_to='static')),
            ],
        ),
    ]
