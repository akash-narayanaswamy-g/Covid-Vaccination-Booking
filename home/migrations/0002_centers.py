# Generated by Django 4.1.5 on 2023-04-20 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='centers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vaccine', models.CharField(max_length=30)),
                ('dose_avva', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.district')),
            ],
        ),
    ]