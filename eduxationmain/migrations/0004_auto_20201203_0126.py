# Generated by Django 3.1.3 on 2020-12-02 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduxationmain', '0003_emailsub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailsub',
            old_name='emailsub',
            new_name='email',
        ),
    ]
