from functools import wraps
from django.http import HttpResponseForbidden
from django_prbac.models import Role

def prbac_required(privilege):
    """
    Decorator for views that checks if the user has the required privilege based on PRBAC.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You are not authenticated to access this resource.")

            # Check if any of the user's roles have the required privilege
            role = Role.objects.get(name=request.user.username)
            privilege_ins = Role.objects.get(name=privilege)
            if role.has_privilege(privilege_ins):
                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden("You do not have permission to access this resource.")

        return _wrapped_view

    return decorator
