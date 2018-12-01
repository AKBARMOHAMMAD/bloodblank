# Generated by Django 2.1.3 on 2018-11-29 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrigranizationRegister',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email_id', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd.City')),
            ],
        ),
        migrations.RemoveField(
            model_name='origanizationregister',
            name='city_name',
        ),
        migrations.AlterField(
            model_name='donorregister',
            name='email_id',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='OriganizationRegister',
        ),
    ]