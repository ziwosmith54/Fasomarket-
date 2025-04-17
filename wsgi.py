import os, sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{project_root.name}.settings_prod')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()