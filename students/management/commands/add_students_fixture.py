from django.core.management.base import BaseCommand
from django.core.management import call_command
from students.models import Student, Group
from django.db import connection

class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Student.objects.all().delete()
        Group.objects.all().delete()

        # Сброс автоинкремента
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE students_group_id_seq RESTART WITH 1;")

        Group.objects.get_or_create(name='Группа 1')
        Group.objects.get_or_create(name='Группа 2')

        call_command('loaddata', 'students_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))