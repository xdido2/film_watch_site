from django.core.files.storage import default_storage
from django.shortcuts import render

from apps.movies.models.history import History
from apps.site_info.models.about import Settings


def user_profile_view(request):
    user = request.user
    history = History.objects.filter(user_id=user.id)
    site_info = Settings.objects.first()

    context = {
        'history': history,
        'site_info': site_info,
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
