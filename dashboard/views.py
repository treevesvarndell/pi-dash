import os
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from rest_framework import views
from rest_framework.response import Response
from subprocess import call


class ScreenView(views.APIView):
    permission_classes = []

    def get(self, request):
        return Response({'testing': True})

    def post(self, request):

        file_path = "/home/pi/dashboard/scripts/monitorToggle.sh"

        if not os.path.isfile(file_path):
            response = Response({'success': False, 'reason': 'File not found'})
        else:
            shell_action = 'on' if request.DATA.get('action', None) == 'on' else 'off'
            system_call = call([file_path, shell_action])
            response = Response({'success': system_call == 0})

        return response


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)