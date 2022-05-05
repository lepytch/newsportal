from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def censor(value):
    bad = ['news', 'breaking', 'lorem']
    final = []
    for w in value.split():
        if w.lower() in bad:
            fin = w.replace(w, '***')
            final.append(fin)
        else:
            final.append(w)
    return f'{" ".join(final)}'


@register.filter
def lower(value):
    return value.lower()
