from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    help = 'Execute a Python script'

    def handle(self, *args, **options):
        # Put your Python script execution code here
        result = subprocess.run(['python', 'E:\sem-5\Copy\iFeels\iFeelsApp\management\commands\inference.py'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        self.stdout.write(self.style.SUCCESS(output))