from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Tag, Book, Volume, Chapter


class ChapterAdmin(NestedStackedInline):
    model = Chapter
    extra = 1


class VolumeAdmin(NestedStackedInline):
   model = Volume
   extra = 1
   inlines = [ChapterAdmin,]


class BookAdmin(NestedModelAdmin):
   model = Book
   search_fields = ['rus_name','eng_name', 'alt_name']
   inlines = [VolumeAdmin,]



admin.site.register(Book, BookAdmin)

admin.site.register(Tag)
admin.site.register(Volume)
admin.site.register(Chapter)
