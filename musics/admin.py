from django.contrib import admin


from musics.models import Music


class MusicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Music, MusicAdmin)

