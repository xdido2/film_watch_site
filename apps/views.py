from django.shortcuts import render


def page_not_found_view(request, exception):
    return render(request, 'films/site-info/404.html', status=404)


def server_error_view(request, exception):
    return render(request, 'films/site-info/500.html', status=500)
