from django.contrib import admin
from .models import Make, Model, Orders, Post, Comment, ContactMessage, Year, Photos


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Orders)
class ObjectAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'pick_up_location', 'delivery_location', 'open_enclosed', 'make', 'model', 'name', 'email',
        'phone_number')
    list_filter = ('open_enclosed', 'pick_up_location', 'delivery_location', 'make', 'model')
    search_fields = ('pick_up_location', 'delivery_location', 'name', 'email', 'phone_number')
    ordering = ('pick_up_location', 'delivery_location')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'user')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'make')
    search_fields = ('name',)
    list_filter = ('make',)
    ordering = ('make', 'name')


@admin.register(Year)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'year')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'message')
    search_fields = ('full_name', 'email', 'phone')


admin.site.register(Photos)
