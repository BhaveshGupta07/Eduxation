# Generated by Django 3.1.3 on 2020-12-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduxationmain', '0002_auto_20201128_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='emailsub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailsub', models.EmailField(max_length=122)),
            ],
        ),
    ]
