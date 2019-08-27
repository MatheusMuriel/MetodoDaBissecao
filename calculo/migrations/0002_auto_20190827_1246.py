# Generated by Django 2.2.4 on 2019-08-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculo',
            name='criterioParada',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='calculo',
            name='epsilon',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='calculo',
            name='funcao',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='calculo',
            name='x1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='calculo',
            name='x2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='calculo',
            name='x3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='calculo',
            name='x4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='calculo',
            name='x5',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='calculo',
            name='xf',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterModelTable(
            name='calculo',
            table='calculo',
        ),
    ]