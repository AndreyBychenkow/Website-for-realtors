from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']
    extra = 1


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']

    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone']
    list_editable = ['new_building']

    list_filter = ['new_building', 'town', 'construction_year', 'active']
    raw_id_fields = ['likes']

    inlines = [OwnerInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']
    list_display = ['user', 'flat', 'created_at']
    search_fields = ['user__username', 'flat__address', 'message']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    list_display = ['name', 'phone_number']
    search_fields = ['name', 'phone_number']
