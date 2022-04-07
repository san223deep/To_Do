from django.contrib import admin
from .models import User, Task
from rest_framework.authtoken.models import Token


class TaskTabular(admin.TabularInline):
    model = Task
    fields = ('title', 'description', 'due_date', 'state')
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = ('username', 'password', 'email', 'first_name', 'last_name', 'date_joined')
    inlines = [TaskTabular]
    readonly_fields = ('date_joined',)

    def save_model(self, request, obj, form, change):
        created = False
        password = form['password'].value()
        obj.set_password(password)
        if obj.pk is None:
            created = True
        super().save_model(request, obj, form, change)
        if created:
            Token.objects.create(user=obj)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'due_date', 'state')
    search_fields = ('title', 'user__username')
    list_filter = ('state', 'due_date')
    list_editable = ('state',)


admin.site.site_header = 'ToDo administration'
admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
