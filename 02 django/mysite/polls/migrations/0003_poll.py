# Generated by Django 5.0 on 2025-04-14 07:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.UUID('da886fb0-63f2-4706-a5e0-27a0409af6fd'), primary_key=True, serialize=False)),
            ],
        ),
    ]
