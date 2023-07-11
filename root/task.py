import requests
from celery import shared_task


@shared_task
def movie_data_form_api():
    from apps.movies.models.movie import Movie
    r_data = requests.get(
        'https://videocdn.tv/api/movies?api_token=V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr&ordering=id&direction=des&page=1&limit=1').json()
    last_page = r_data.get('last_page', 0)

    for page in range(1, last_page + 1):
        data = requests.get(
            f'https://videocdn.tv/api/movies?api_token=V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr&ordering=id&direction=des&page={page}&limit=100').json()
        movie_data = data.get('data', [])

        for content in movie_data:
            objects = {
                'ru_title': content.get('ru_title', ''),
                'orig_title': content.get('orig_title', ''),
                'released': content.get('released', ''),
                'iframe_src': 'https:' + content.get('iframe_src', ''),
            }

            if not Movie.objects.filter(orig_title=objects['orig_title'],
                                        ru_title=objects['ru_title']).exists() and objects is not None:
                Movie.objects.create(**objects)

# import requests
#
# from celery import shared_task
#
# from apps.movies.models.movie import Movie
#
#
# @shared_task
# def movie_data_form_api():
#     r_data = requests.get(
#         'https://videocdn.tv/api/movies?api_token=V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr&ordering=id&direction=des&page=1&limit=1').json()
#     for page in range(1, r_data['last_page']):
#         data = requests.get(
#             f'https://videocdn.tv/api/movies?api_token=V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr&ordering=id&direction=des&page={page}&limit=100').json()
#         for i in range(len(data)):
#             content = data['data'][i]
#             objects = {'ru_title': content['ru_title'],
#                        'orig_title': content['orig_title'],
#                        'released': content['released'],
#                        'iframe_src': 'https:' + content['iframe_src']}
#             if not Movie.objects.filter(orig_title=content['orig_title'],
#                                         ru_title=content['ru_title']).exists() and objects is not None:
#                 Movie.objects.create(**objects)
