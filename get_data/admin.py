from django.contrib import admin
from .models import Party, PartyPolicy, City, Gungu, Candidate
# Register your models here.


class PartyPolicyAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'title','category')


class GunguAdmin(admin.ModelAdmin):
    list_display = ('sd_name', 'name', 'sgg_name',)



# def pusan_filter(modeladmin, request, queryset):
#     pusan_gungu = Gungu.objects.filter(sd_name = City.objects.get(name='부산광역시'))
#     pusan_queryset = queryset.filter(sggname=pusan_gungu)
#     return pusan_queryset
# pusan_filter.short_description = "here is pusan filter!"


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('candi_id','name','sggname','jdname','promise4','promise5','promise3','promise1','promise6','promise2')
    list_editable = ('promise1','promise2','promise3','promise4','promise5','promise6')
    # actions = [pusan_filter]
    list_filter = ('sggname',)
admin.site.register(Party)

admin.site.register(PartyPolicy, PartyPolicyAdmin)
admin.site.register(City)

admin.site.register(Gungu, GunguAdmin)
admin.site.register(Candidate, CandidateAdmin)
