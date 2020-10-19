# Generated by Django 3.1.1 on 2020-10-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/authors')),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
    ]
