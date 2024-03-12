# Generated by Django 4.1.13 on 2024-03-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_menu_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='toppings',
        ),
        migrations.AddField(
            model_name='menu',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='home.topping'),
        ),
    ]
