from django.db import migrations, models


def fill_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    Flat.objects.filter(construction_year__isnull=False).update(
        new_building=models.F('construction_year') >= 2015
    )

    Flat.objects.filter(construction_year__isnull=True).update(new_building=False)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0004_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building),
    ]
