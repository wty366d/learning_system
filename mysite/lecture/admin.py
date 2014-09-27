from django.contrib import admin

# Register your models here.
from lecture.models import Lecture

class LectureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['lecture_id','lecture']}),
        ('Date information', {'fields': ['term']}),
    ]
    #inlines
    
    list_display = ('lecture_id','lecture','term')
    list_filter = ['term']
    search_fields = ['lecture']

admin.site.register(Lecture, LectureAdmin)
