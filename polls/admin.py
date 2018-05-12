from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

'''
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5
'''

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date']}),
]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Name',{'fields':['question']}),
        ('Choice Name',  {'fields':['choice_text']}),
        ('Votes',        {'fields':['votes']}),
        ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
