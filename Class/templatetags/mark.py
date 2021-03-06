from django import template
from django.template.defaultfilters import stringfilter

import markdown

register = template.Library()


@register.filter()
@stringfilter
def md(value):
    return markdown.markdown(value)
