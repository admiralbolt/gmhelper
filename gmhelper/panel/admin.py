from django.contrib import admin

from panel.models import Song, SongTag

admin.site.register(SongTag)
admin.site.register(Song)
