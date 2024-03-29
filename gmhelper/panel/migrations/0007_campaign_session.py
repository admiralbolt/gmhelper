# Generated by Django 2.2.1 on 2019-08-18 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_auto_20190818_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('flavor', models.TextField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('flavor', models.TextField(blank=True, default=None)),
                ('content', models.TextField(blank=True, default=None)),
                ('reflection', models.TextField(blank=True, default=None)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Campaign')),
                ('images', models.ManyToManyField(blank=True, to='panel.Image')),
                ('letters', models.ManyToManyField(blank=True, to='panel.Letter')),
                ('lores', models.ManyToManyField(blank=True, to='panel.Lore')),
                ('songs', models.ManyToManyField(blank=True, to='panel.Song')),
            ],
        ),
    ]
