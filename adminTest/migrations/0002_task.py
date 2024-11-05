# Generated by Django 5.1.2 on 2024-11-05 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminTest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
