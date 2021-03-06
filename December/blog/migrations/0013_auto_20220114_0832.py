# Generated by Django 3.1.14 on 2022-01-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_comment_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(default='published', max_length=16),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='url',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='password',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(default='post', max_length=16),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
