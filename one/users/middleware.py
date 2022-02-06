import datetime

from django.conf import settings
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin


class ActiveUserMiddleware(MiddlewareMixin):
    """User Middleware"""

    def process_request(self, request):
        """
        1. Set cache for last seen user
        :param request:
        :return:
        """
        try:
            current_user = request.user
            if current_user.is_authenticated:
                now = datetime.datetime.now()
                cache.set(
                    "seen_%s" % (current_user.username),
                    now,
                    settings.USER_LASTSEEN_TIMEOUT,
                )
        except Exception:
            pass
