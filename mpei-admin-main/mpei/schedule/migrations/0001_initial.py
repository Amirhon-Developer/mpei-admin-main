# Generated by Django 4.1.7 on 2023-03-26 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('code', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('year', models.IntegerField(choices=[(0, 'Unknown'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')], default=0)),
                ('file', models.FileField(blank=True, null=True, upload_to='pics')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.department')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
