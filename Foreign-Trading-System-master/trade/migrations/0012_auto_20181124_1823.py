# Generated by Django 2.1.3 on 2018-11-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0011_auto_20181124_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='requestID',
        ),
        migrations.AddField(
            model_name='request',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
