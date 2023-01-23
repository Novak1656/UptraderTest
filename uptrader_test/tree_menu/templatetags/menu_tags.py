from django.template import Library

register = Library()


@register.inclusion_tag('tree_menu/menu.html')
def draw_menu(name: str = 'Menu'):
    return {'name': name}
