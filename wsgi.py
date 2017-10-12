import os
import sys
# Add the app's directory to the PYTHONPATH
sys.path.append('~/httpdocs/quiz')
os.environ['DJANGO_SETTINGS_MODULE'] = 'quiz.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
