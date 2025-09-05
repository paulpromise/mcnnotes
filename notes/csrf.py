from django.conf import settings
from django.middleware.csrf import CsrfViewMiddleware as DjangoCsrfViewMiddleware
import logging

logger = logging.getLogger(__name__)

class CustomCsrfMiddleware(DjangoCsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        # Skip CSRF validation for Azure health check endpoints
        if request.path == '/robots933456.txt':
            return None
            
        # Log CSRF related information
        logger.info(f"Request path: {request.path}")
        logger.info(f"CSRF Cookie: {request.COOKIES.get(settings.CSRF_COOKIE_NAME)}")
        logger.info(f"CSRF Token in POST: {request.POST.get('csrfmiddlewaretoken')}")
        logger.info(f"X-CSRFToken header: {request.headers.get('X-CSRFToken')}")
        logger.info(f"Referer: {request.headers.get('Referer')}")
        
        # Allow requests from trusted origins
        referer = request.headers.get('Referer', '')
        if any(trusted in referer for trusted in settings.CSRF_TRUSTED_ORIGINS):
            return None
            
        return super().process_view(request, callback, callback_args, callback_kwargs)

    def _reject(self, request, reason):
        logger.error(f"CSRF Rejection for {request.path}: {reason}")
        logger.error(f"Headers: {dict(request.headers)}")
        return super()._reject(request, reason)
