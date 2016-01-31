import os
import re
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from rest_framework import views
from rest_framework.response import Response
from subprocess import call, check_output


class ScreenApiView(views.APIView):
    permission_classes = []
    file_path = "/home/pi/dashboard/scripts/monitorToggle.sh"

    def get(self, request):

        if not os.path.isfile(self.file_path):
            tv_status = 'error'
        else:
            status_check = check_output([self.file_path, 'status'])
            if re.compile("TV is off").search(status_check):
                tv_status = 'off'
            else:
                tv_status = 'on'

        return Response({'status': tv_status})

    def post(self, request):

        if not os.path.isfile(self.file_path):
            response = Response({'success': False, 'reason': 'File not found'})
        else:
            shell_action = 'on' if request.DATA.get('action', None) == 'on' else 'off'
            system_call = call([self.file_path, shell_action])
            response = Response({'success': system_call == 0})

        return response


class ScreenView(TemplateView):
    template_name = 'screen.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(ScreenView, self).dispatch(*args, **kwargs)


class IndexView(TemplateView):
    template_name = 'departure-board.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)