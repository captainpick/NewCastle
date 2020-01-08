# Generated by Django 3.0 on 2019-12-02 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('gender', models.CharField(choices=[('M', 'مذکر'), ('F', 'مونث')], default=None, max_length=1, null=True)),
                ('warden', models.CharField(blank=True, max_length=100)),
                ('caretaker', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=255)),
                ('room_type', models.CharField(choices=[('2', 'دو تخته'), ('3', '۳ تخته'), ('4', '۴ تخته')], default=None, max_length=1)),
                ('vacant', models.BooleanField(default=False)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.Hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('cell_phone', models.CharField(max_length=10)),
                ('SSN', models.CharField(max_length=10)),
                ('Address', models.TextField()),
                ('profile', models.ImageField(upload_to='imgs/')),
                ('room_alotted', models.BooleanField(default=False)),
                ('Room', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Room.Room')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='reserved_for_specific_user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Room.Users'),
        ),
    ]