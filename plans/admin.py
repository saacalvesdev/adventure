from django.contrib import admin
from .models import Plans

class ListPlans(admin.ModelAdmin):
    list_display = ('title', 'type_plan', 'value')

admin.site.register(Plans, ListPlans)

