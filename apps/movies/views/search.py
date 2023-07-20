from django.core.paginator import Paginator
from django.shortcuts import render, redirect


def search_view(request):
    query = request.GET.get('q')
    data = []
    if query == '':
        return redirect('film-list')
    else:
        from movies.documents import MoviesIndex

        s = MoviesIndex.search().query("multi_match", query=query, fields=["*"])

        for hit in s:
            data.append(hit)

        p = Paginator(data, 18)
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)

        context = {
            'total_count_movie': len(data),
            'page_obj': page_obj,
        }
        return render(request, 'films/main_content/search.html', context)
