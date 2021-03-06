# Generated by Django 4.0.3 on 2022-03-10 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_answer',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_choice', to='survey.choice'),
        ),
        migrations.AlterField(
            model_name='user_answer',
            name='text_answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
