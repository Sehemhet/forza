from django import template
from home.models import *

register = template.Library()


@register.simple_tag()
def get_partners():
    return Footer.objects.all()