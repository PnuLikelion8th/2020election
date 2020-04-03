from django.contrib import admin
from .models import Party, PartyPolicy, City, Gungu, Candidate
# Register your models here.


class PartyPolicyAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'title','category')


class GunguAdmin(admin.ModelAdmin):
    list_display = ('sd_name', 'name', 'sgg_name',)


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('candi_id','name','sggname','giho_num','jdname','age','job','edu','career1','career2')

admin.site.register(Party)

admin.site.register(PartyPolicy, PartyPolicyAdmin)
admin.site.register(City)

admin.site.register(Gungu, GunguAdmin)
admin.site.register(Candidate, CandidateAdmin)
