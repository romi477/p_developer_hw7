from django.http import HttpResponse



def test(request):
    # return HttpResponse(f'<div>{request.method}</div>\n\n{dir(request)}')
    return HttpResponse(f'<div>{request.method}</div>\n\n{request.environ}')