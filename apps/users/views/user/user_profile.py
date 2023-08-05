from django.core.files.storage import default_storage
from django.shortcuts import render

from apps.movies.models.history import History
from apps.site_info.models.about import Settings
from apps.movies.models.comment import Comment
from apps.movies.models.movie import Genre, ReleaseYear


def user_profile_view(request):
    user = request.user
    last_comments = Comment.objects.filter(is_approved=True)[:2]
    release_years = ReleaseYear.objects.all()
    genres = Genre.objects.all()
    history = History.objects.filter(user_id=user.id)
    site_info = Settings.objects.first()

    context = {
        'history': history,
        'site_info': site_info,
        'last_comments': last_comments,
        'release_years': release_years,
        'genres': genres,
        'user': user,
    }
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        if avatar:
            unique_filename = f'user_avatar_{user.id}'

            avatar_path = default_storage.save(
                f'users/avatars/{unique_filename}',
                avatar.file
            )

            user.avatar = avatar_path
            user.save()

    return render(request, 'films/user/user-profile.html', context)
