import datetime

from django.conf import settings
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin


class ActiveUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            current_user = request.user
            if request.user.is_authenticated:
                now = datetime.datetime.now()
                cache.set(
                    "seen_%s" % (current_user.username),
                    now,
                    settings.USER_LASTSEEN_TIMEOUT,
                )
        except Exception:
            pass
