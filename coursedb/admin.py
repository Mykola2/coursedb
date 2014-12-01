__author__ = 'Eric'
from django.contrib import admin
from qanda.models import Question,Tag,Answer


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)