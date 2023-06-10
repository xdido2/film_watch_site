from django.shortcuts import render

from apps.site_info.models.about import Settings


def film_detail_view(request):
    data = Settings.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'films/main_content/base.html', context)
