from django.contrib import admin

from wtfhack.base.models import Repo

class RepoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['url', 'language', 'description', 'full_name']})
    ]

admin.site.register(Repo, RepoAdmin)