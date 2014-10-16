from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    # creates 2 extra lines
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    # ensures that the table info is shown inline
    inlines = [ChoiceInline]
    
    
admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)