from django.template import Library, RequestContext
from ..models import Menu

register = Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str = 'main_menu'):
    cur_section = context.request.GET.get('section')
    menu_queryset = Menu.objects.select_related('category', 'parent').filter(category__systemic_name=name)

    if len(menu_queryset) == 0:
        return {'name': name}

    menu_name = menu_queryset.first().category.name
    menu_data = {section: None for section in menu_queryset if not section.parent}

    if not cur_section:
        return {'name': menu_name, 'menu': menu_data}

    active_section = None
    for section in menu_queryset:
        if section.link != cur_section:
            continue
        active_section = section
        break

    post_sections = {post_sect: None for post_sect in menu_queryset if post_sect.parent == active_section}
    first_section = active_section

    active_sections = list()
    while active_section.parent:
        for sect in menu_queryset:
            if sect == active_section.parent:
                active_section = sect
                active_sections.append(sect)
                break
    if active_sections:
        first_section = active_sections[::-1][0]

    def generate_tree_data(section) -> dict:
        section_data = {section: dict()}
        for sect_obj in menu_queryset:
            if section == sect_obj.parent:
                if sect_obj in active_sections:
                    section_data[section].update(generate_tree_data(sect_obj))
                    continue
                section_data[section].update({sect_obj: None})
                if sect_obj.link == cur_section:
                    section_data[section].update({sect_obj: post_sections})
        return section_data

    data = generate_tree_data(first_section)
    menu_data.update({first_section: data[first_section]})
    return {'name': menu_name, 'menu': menu_data, 'cur_section': cur_section}
