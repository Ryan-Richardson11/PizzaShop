# Generated by Django 4.1.13 on 2024-03-21 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_size_alter_menu_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.size'),
        ),
    ]
