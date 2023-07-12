from django.shortcuts import render

from apps.users.forms.user_profile import UserProfileForm


def user_profile_view(request):
    user = request.user
    context = {
        'user': user,
    }
    if request.method == 'POST':
        forms_profile = UserProfileForm(request.POST)
        if forms_profile.is_valid():
            username = forms_profile.data.get('username')
            email = forms_profile.data.get('email')
            if username:
                user.username = username
                user.save()
            elif email:
                user.email = email
                user.save()
        else:
            context['errors_userprofile'] = forms_profile.errors

    return render(request, 'films/user/user-profile.html', context)
