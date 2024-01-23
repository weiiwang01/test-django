import json
import os

from django.http import JsonResponse

from .models import Visitor


def index(request):
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    Visitor.objects.create(user_agent=user_agent)
    total_visitors = Visitor.objects.count()
    return JsonResponse({"visitors": total_visitors})


def debug(request):
    return JsonResponse({"environ": json.dumps(dict(os.environ))})
