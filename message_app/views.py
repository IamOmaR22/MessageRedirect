from django.shortcuts import render

def index(request):
    error_message = request.GET.get('error', None)
    return render(request, 'index.html', {'error_message': error_message})

def message_redirect(request):
    code = request.GET.get('c')
    if code:
        return render(request, 'redirect.html', {'code': code})
    else:
        error_message = "Missing 'c' parameter"
        return render(request, 'index.html', {'error_message': error_message})
