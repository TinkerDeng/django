"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

# python应用程序和框架和web服务器之间的接口
# 测试的时候是djongo起的轻量级的服务器，真正上线的时候通常需要一个大型的服务器，丽日apache，tomcat
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
