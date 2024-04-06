from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect


def index(request):
    error_message = request.GET.get('error', None)
    return render(request, 'index.html', {'error_message': error_message})

# def message_redirect(request):
#     code = request.GET.get('c')
#     if code:
#         return render(request, 'redirect.html', {'code': code})
#     else:
#         error_message = "Missing 'c' parameter"
#         return render(request, 'index.html', {'error_message': error_message})

def send_sms(request):
    code = request.GET.get('c', '')
    if not code:
        return HttpResponse('Missing message parameter', status=400)

    # Construct the SMS URL
    sms_url = "sms:888222?body=%s" % code
    return render(request, 'send_sms.html', {'sms_url': sms_url})
