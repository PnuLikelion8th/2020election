from django.contrib import admin
from .models import Party,PartyPolicy,City,Gungu
# Register your models here.


class PartyPolicyAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'title','category')


class GunguAdmin(admin.ModelAdmin):
    list_display = ('sd_name', 'name', 'sgg_name',)


admin.site.register(Party)

admin.site.register(PartyPolicy, PartyPolicyAdmin)
admin.site.register(City)

admin.site.register(Gungu, GunguAdmin)
