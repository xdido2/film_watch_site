from django.core.files.storage import default_storage
from django.shortcuts import render

from apps.users.models.history import History


def user_profile_view(request):
    user = request.user
    history = History.objects.filter(user_id=user.id)

    context = {
        'history': history,
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
