# Generated by Django 4.1.5 on 2023-01-24 20:37

from django.db import migrations


def create_test_menu(apps, schema_editor):
    MenuCategories = apps.get_model('tree_menu', 'MenuCategories')
    Menu = apps.get_model('tree_menu', 'Menu')

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


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0002_alter_menu_link_alter_menu_parent'),
    ]

    operations = [
        migrations.RunPython(create_test_menu)
    ]
