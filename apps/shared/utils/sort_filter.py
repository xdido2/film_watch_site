def movie_sort_filter(_filter, movies, year):
    sort_filter = movies
    if _filter == 'popular':
        if year:
            sort_filter = movies.filter(release_year__year=year).order_by('-vote')
            _filter = 'Популярные(IMDB)'
        else:
            sort_filter = movies.order_by('-vote')
            _filter = 'Популярные(IMDB)'
    elif _filter == 'news':
        if year:
            sort_filter = movies.filter(release_year__year=year).order_by('-release_year__year')
            _filter = 'Новинки'
        else:
            sort_filter = movies.order_by('-release_year__year')
            _filter = 'Новинки'
    elif _filter == 'decrease':
        if year:
            sort_filter = movies.filter(release_year__year=year).order_by('ru_title')
            _filter = 'От А до Я'
        else:
            sort_filter = movies.order_by('ru_title')
            _filter = 'От А до Я'

    elif _filter == 'increase':
        if year:
            sort_filter = movies.filter(release_year__year=year).order_by('-ru_title')
            _filter = 'От Я до А'
        else:
            sort_filter = movies.order_by('-ru_title')
            _filter = 'От Я до А'

    elif _filter == 'lasts':
        if year:
            sort_filter = movies.filter(release_year__year=year).order_by('-created_at')
            _filter = 'Последние'
        else:
            sort_filter = movies.order_by('-created_at')
            _filter = 'Последние'

    elif year:
        sort_filter = movies.filter(release_year__year=year)

    return sort_filter, _filter
