import sys, site, os

vepath = '/home/apreche/.virtualenvs/openducats.org/lib/python2.5/site-packages'

prev_sys_path = list(sys.path)
site.addsitedir(vepath)
sys.path.append('/home/apreche/.virtualenvs/openducats.org/')

new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

from django.core.handlers.wsgi import WSGIHandler
os.environ['DJANGO_SETTINGS_MODULE'] = 'ducats.settings'
application = WSGIHandler()
