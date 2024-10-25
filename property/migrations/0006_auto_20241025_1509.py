# Generated by Django 5.1.2 on 2024-10-25 12:09

from django.db import migrations


def fill_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year is not None:
            flat.new_building = flat.construction_year >= 2015
        else:
            flat.new_building = False
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0005_auto_20241025_1445'),
    ]

    operations = [
        migrations.RunPython(fill_new_building),
    ]
