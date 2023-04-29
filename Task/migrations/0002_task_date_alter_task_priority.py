# Generated by Django 4.2 on 2023-04-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('medium', 'medium'), ('low', 'low'), ('high', 'high')], max_length=20, verbose_name='Priority'),
        ),
    ]