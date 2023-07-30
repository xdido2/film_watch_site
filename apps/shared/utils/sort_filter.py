def movie_sort_filter(_filter, movies, year):
    sort_filter = movies
    if _filter == 'popular':
        if year:
            sort_filter = movies.filter(release_year__year=year, release_year__year__isnull=False).order_by('-vote_count')
            _filter = 'Популярные(IMDB)'
        else:
            sort_filter = movies.filter(release_year__year__isnull=False).order_by('-vote_count')
            _filter = 'Популярные(IMDB)'
    elif _filter == 'news':
        if year:
            sort_filter = movies.filter(release_year__year=year).order_by('-release_year__year')
            _filter = 'Новинки'
        else:
            sort_filter = movies.order_by('-release_year__year').filter(release_year__year__isnull=False)
            _filter = 'Новинки'
    elif _filter == 'decrease':
        if year:
            sort_filter = movies.filter(release_year__year=year, release_year__year__isnull=False).order_by('ru_title')
            _filter = 'От А до Я'
        else:
            sort_filter = movies.filter(release_year__year__isnull=False).order_by('ru_title')
            _filter = 'От А до Я'

    elif _filter == 'increase':
        if year:
            sort_filter = movies.filter(release_year__year=year, release_year__year__isnull=False).order_by('-ru_title')
            _filter = 'От Я до А'
        else:
            sort_filter = movies.filter(release_year__year__isnull=False).order_by('-ru_title')
            _filter = 'От Я до А'

    elif _filter == 'lasts':
        if year:
            sort_filter = movies.filter(release_year__year=year, release_year__year__isnull=False).order_by('-created_at')
            _filter = 'Последние'
        else:
            sort_filter = movies.filter(release_year__year__isnull=False).order_by('-created_at')
            _filter = 'Последние'

    elif year:
        sort_filter = movies.filter(release_year__year=year, release_year__year__isnull=False)

    return sort_filter, _filter
