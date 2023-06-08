import requests
from celery import shared_task

from movies.models.movie import Movie



@shared_task
def movie_data_form_api():
    r_data = requests.get(
        'https://videocdn.tv/api/movies?api_token=V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr&ordering=id&direction=des&page=1&limit=1').json()
    for page in range(1, r_data['last_page']):
        data = requests.get(
            f'https://videocdn.tv/api/movies?api_token=V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr&ordering=id&direction=des&page={page}&limit=100').json()
        for i in range(len(data)):
            contant = data['data'][i]
            objects = {'ru_title': contant['ru_title'], 'orig_title': contant['orig_title'],
                       'released': contant['released'],
                       'iframe_src': 'https:' + contant['iframe_src']}
            if not Movie.objects.filter(orig_title=contant['orig_title'], ru_title=contant['ru_title']).exists():
                Movie.objects.create(**objects)
