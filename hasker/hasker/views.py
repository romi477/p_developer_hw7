from django.shortcuts import redirect


def redirect_index(request):
    return redirect('index', permanent=True)
