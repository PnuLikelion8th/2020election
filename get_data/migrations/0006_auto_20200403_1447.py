# Generated by Django 2.2.7 on 2020-04-03 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0005_candidate_giho_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='sdname',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='wiwname',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='jdname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_data.Party'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='sggname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_data.Gungu'),
        ),
    ]
