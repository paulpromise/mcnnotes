from django.conf import settings
from django.middleware.csrf import CsrfViewMiddleware as DjangoCsrfViewMiddleware
import logging

logger = logging.getLogger(__name__)

class CustomCsrfMiddleware(DjangoCsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        # Log CSRF related headers and cookies for debugging
        logger.info(f"Request path: {request.path}")
        logger.info(f"CSRF Cookie: {request.COOKIES.get(settings.CSRF_COOKIE_NAME)}")
        logger.info(f"CSRF Token in POST: {request.POST.get('csrfmiddlewaretoken')}")
        logger.info(f"Request Headers: {dict(request.headers)}")
        
        return super().process_view(request, callback, callback_args, callback_kwargs)

    def _reject(self, request, reason):
        logger.error(f"CSRF Rejection: {reason}")
        return super()._reject(request, reason)
