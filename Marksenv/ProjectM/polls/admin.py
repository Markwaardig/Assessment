from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    # number of extra lines available
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')	# specifies the sequence of display
    list_filter = ['pub_date']	# ensures that filter is being displayed
    search_fields = ['question_text']	# is showing filter function on top of the page
    inlines = [ChoiceInline]	# ensures that the table info is shown inline
    
    
admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)