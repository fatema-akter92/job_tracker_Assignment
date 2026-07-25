from datetime import datetime


class RequestLoggerMiddleware:
    """
    Custom middleware that logs the date/time, HTTP method, and
    requested URL path for every incoming request.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now().strftime('%Y-%m-%d %I:%M %p')
        print('---------------------------------')
        print(f'Time   : {now}')
        print(f'Method : {request.method}')
        print(f'Path   : {request.path}')
        print('---------------------------------')

        response = self.get_response(request)
        return response
