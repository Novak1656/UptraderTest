from django.core.management import BaseCommand
from tree_menu.models import Menu, MenuCategories


class Command(BaseCommand):
    help = 'Команда для создания тестовой менюшки'

    def handle(self, *args, **options):
        category, _ = MenuCategories.objects.get_or_create(name='Главное меню', systemic_name='main_menu')

        sect_1 = Menu.objects.create(name='Section 1', category=category, link='section_1')
        Menu.objects.create(name='Section 1.1', category=category, link='section_1_1', parent=sect_1)

        sect_2 = Menu.objects.create(name='Section 2', category=category, link='section_2')
        sect_2_1 = Menu.objects.create(name='Section 2.1', category=category, link='section_2_1', parent=sect_2)
        sect_2_1_1 = Menu.objects.create(name='Section 2.1.1', category=category, link='section_2_1_1', parent=sect_2_1)
        Menu.objects.create(name='Section 2.2', category=category, link='section_2_2', parent=sect_2_1_1)

        sect_3 = Menu.objects.create(name='Section 3', category=category, link='section_3')
        Menu.objects.create(name='Section 3.1', category=category, link='section_3_1', parent=sect_3)
        Menu.objects.create(name='Section 3.2', category=category, link='section_3_2', parent=sect_3)
        Menu.objects.create(name='Section 3.3', category=category, link='section_3_3', parent=sect_3)
        print('Test menu has been created.')
