from django.db import migrations
from phonenumbers import parse, is_valid_number, format_number, PhoneNumberFormat
from phonenumbers.phonenumberutil import NumberParseException


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    flats_to_update = []

    for flat in flats:
        normalized_phone = normalize_phone(flat.owners_phonenumber)
        if normalized_phone is not None:
            flat.owner_pure_phone = normalized_phone
            flats_to_update.append(flat)

    Flat.objects.bulk_update(flats_to_update, ['owner_pure_phone'])


def normalize_phone(phone_number):
    if not phone_number:
        return None

    try:
        parsed_number = parse(phone_number, 'RU')
        if is_valid_number(parsed_number):
            return format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
    except NumberParseException:
        pass

    return None


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0009_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]
