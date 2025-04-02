import os
import sys

# Ensure Django finds the correct project path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyActualProject.settings')  # Make sure this is correct
    execute_from_command_line(sys.argv)
