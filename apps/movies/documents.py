from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl import Index
from django_elasticsearch_dsl.search import Search

from apps.movies.models.movie import Movie

movieIndex = Index('movie')


@movieIndex.document
class MoviesIndex(Document):
    slug_link = fields.KeywordField(attr='slug_link')

    class Django:
        model = Movie
        fields = ['orig_title', 'ru_title', 'poster', 'vote']

    @classmethod
    def generate_id(cls, article):
        return article.slug_link
