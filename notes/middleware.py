from django.middleware.csrf import CsrfViewMiddleware

class DebugCsrfMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        retval = super().process_view(request, callback, callback_args, callback_kwargs)
        # If csrf failed, log information for debugging
        if retval:
            print("CSRF Failed: Referer: %s" % request.META.get('HTTP_REFERER', ''))
            print("CSRF Failed: URL: %s" % request.path)
            print("CSRF Failed: Cookie: %s" % request.META.get('CSRF_COOKIE', ''))
            print("CSRF Failed: Post Token: %s" % request.POST.get('csrfmiddlewaretoken', ''))
        return retval
