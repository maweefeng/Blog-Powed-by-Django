# Generated by Django 2.0 on 2019-05-24 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('aritcle_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('brief_content', models.TextField()),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
