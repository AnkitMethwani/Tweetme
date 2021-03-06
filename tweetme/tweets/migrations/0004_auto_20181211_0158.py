# Generated by Django 2.1.4 on 2018-12-11 09:58

from django.db import migrations, models
import tweets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_tweet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140, validators=[tweets.validators.validate_content]),
        ),
    ]
