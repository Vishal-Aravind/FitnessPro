# accounts/admin.py

from django.contrib import admin
from .models import Account
from dietwork.models import DietPlan, WorkoutPlan

class DietPlanInline(admin.TabularInline):
    model = DietPlan
    extra = 1
    fields = ['excel_link', 'meal_details',  'date']

class WorkoutPlanInline(admin.TabularInline):
    model = WorkoutPlan
    extra = 1
    fields = ['excel_link', 'workout_details', 'date']

class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'batch', 'phone_number', 'height', 'weight', 'date_joined')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    inlines = [DietPlanInline, WorkoutPlanInline]

# admin.site.register(Account, AccountAdmin)
