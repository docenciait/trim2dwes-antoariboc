# Generated by Django 5.1.5 on 2025-02-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='categoria',
            field=models.CharField(choices=[('bache', 'bache'), ('alumbrado', 'alumbrado'), ('basura', 'basura'), ('otro', 'otro')], default='otro', max_length=20),
        ),
    ]
