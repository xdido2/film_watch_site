from django.shortcuts import redirect


def anonymous_required(redirect_url):
    """
    Decorator for views that allow only unauthenticated users to access view.

    Usage:

    @anonymous_required(redirect_url='/')
    def homepage(request):
        return render(request, 'homepage.html')
    """

    def _wrapped(view_func, *args, **kwargs):
        def check_anonymous(request, *args, **kwargs):
            view = view_func(request, *args, **kwargs)
            if request.user.is_authenticated:
                return redirect(redirect_url)
            return view

        return check_anonymous

    return _wrapped
