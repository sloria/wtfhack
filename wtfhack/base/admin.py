from django.contrib import admin

from wtfhack.base.models import Repo, Language

class RepoInline(admin.TabularInline):
    model = Repo
class RepoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['url', 'language', 'description', 'full_name']})
    ]

class LanguageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'learn_url' ]})
    ]
    inlines = [RepoInline,]

admin.site.register(Repo, RepoAdmin)
admin.site.register(Language, LanguageAdmin)
