from django.contrib import admin

# Register your models here.
from history.models import History


class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['lecture','student']}),
        ('Date information', {'fields': ['year']}),
        ('Grade information', {'fields': ['grade']}),
    ]
    #inlines
    
    list_display = ('lecture','student','year','grade')
    list_filter = ['student','lecture','year']
    search_fields = ['lecture']

admin.site.register(History, HistoryAdmin)
