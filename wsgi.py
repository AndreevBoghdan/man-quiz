import os
import sys
import site
# Add the app's directory to the PYTHONPATH
site.addsitedir('~/httpdocs/quiz/.quizenv/local/lib/python2.7/site-packages')
sys.path.append('~/httpdocs/quiz')
os.environ['DJANGO_SETTINGS_MODULE'] = 'quiz.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
