__author__ = 'franciscui'
#!/usr/bin/env python
# coding: utf-8

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')
os.environ['DJANGO_SETTINGS_MODULE']='ldapapi.settings'
from django.core.wsgi import get_wsgi_application  
application = get_wsgi_application()