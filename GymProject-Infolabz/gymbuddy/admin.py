from django.contrib import admin
from .models import (
    User, Country, State, City, WorkoutCategory,
    WorkoutExercise, Subscription, UserSubscription,
    Payment, UserFeedback, ContactUs
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name',)
    list_filter = ('country',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name',)
    list_filter = ('state',)

@admin.register(WorkoutCategory)
class WorkoutCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','category_photo')
    search_fields = ('name',)

@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'duration_in_min', 'created_at', 'excercise_photo')
    search_fields = ('title', 'category__name')
    list_filter = ('category', 'difficulty')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_month', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'is_active', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'plan__name')
    list_filter = ('is_active',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_date', 'payment_method', 'status')
    search_fields = ('user__first_name', 'user__last_name', 'amount')
    list_filter = ('payment_method', 'status')

@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'message', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'subject__name')

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')
    search_fields = ('name', 'email', 'phone')
