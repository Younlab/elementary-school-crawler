# Generated by Django 2.2 on 2019-04-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='category',
            field=models.CharField(choices=[('n', '공지사항'), ('p', '가정통신문')], max_length=40),
        ),
    ]
