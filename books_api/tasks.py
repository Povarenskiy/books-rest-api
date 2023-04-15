from core.celery import app
from django.db.models import F

from .models import Chapter


@app.task
def inc_chapter_field(pk, field):
    """
    Функция увеличивает на 1 значение поля экземпляра Chapter
    """
    param = {field: F(field) + 1}
    Chapter.objects.filter(pk=pk).update(**param)
        

    
