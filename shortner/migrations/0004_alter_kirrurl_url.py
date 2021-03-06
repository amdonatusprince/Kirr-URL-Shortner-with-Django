# Generated by Django 3.2.3 on 2021-06-13 17:57

from django.db import migrations, models
import shortner.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_kirrurl_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortner.validators.validate_url, shortner.validators.validate_dot_com]),
        ),
    ]
