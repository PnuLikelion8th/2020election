from django.contrib import admin
from .models import Party,PartyPolicy,City
# Register your models here.


class PartyPolicyAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'title','category')



admin.site.register(Party)

admin.site.register(PartyPolicy, PartyPolicyAdmin)
admin.site.register(City)