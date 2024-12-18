# Generated by Django 5.1.2 on 2024-10-25 15:41

from django.db import migrations


def transfer_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all().iterator():
        owner, created = Owner.objects.get_or_create(
            name=flat.owner,
            phone_number=flat.owners_phonenumber
        )
        owner.flats.add(flat)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0011_owner'),
    ]

    operations = [
        migrations.RunPython(transfer_owners),
    ]
