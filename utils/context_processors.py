from info.models import PersInfo

def info_context(request):
    header_info = PersInfo.objects.first()
    return {'h_info': header_info}

def current_url(request):
    return {
    'current_url': request.path,
    }