from django.contrib import admin

# Register your models here.
from .models import *


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Meta Data', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date', 'was_Published_Recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    #list_per_page = 1


admin.site.register(Question, QuestionAdmin)



admin.site.register(Choice)