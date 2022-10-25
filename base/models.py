from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class Nota(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, primary_key=True)
    nota = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.alumno.nombre}: {self.nota}'
    
    
# wagtail
class FaqPage(Page):
    max_count = 1
    
    parent_page_type = [
        'wagtailcore.Page'
    ]
    subpage_types = [
        'base.Faq',  # appname.ModelName
    ]


class AboutPage(Page):
    max_count = 1
    
    parent_page_type = [
        'wagtailcore.Page'
    ]
    subpage_types = [
        'base.About',  # appname.ModelName
    ]


class Faq(Page):
    question = models.CharField(max_length = 255)
    body = RichTextField()
    
    content_panels = Page.content_panels + [
        FieldPanel('question'),
        FieldPanel('body')
    ]
    
    subpage_types = []
    parent_page_type = [
        'FaqPage.Page'
    ]
    

class About(Page):
    max_count = 1
    
    body = RichTextField()
    
    parent_page_type = [
        'AboutPage.Page'
    ]
    subpage_types = []
    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]