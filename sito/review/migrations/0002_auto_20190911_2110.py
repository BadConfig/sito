# Generated by Django 2.2.4 on 2019-09-11 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userAccount',
            fields=[
                ('userID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='program',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='review.candidates'),
        ),
        migrations.AddField(
            model_name='candidates',
            name='accountData',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='authModel', to='review.userAccount'),
            preserve_default=False,
        ),
    ]
