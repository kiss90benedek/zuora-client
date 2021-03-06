"""
Transport for Zuora SOAP API
"""
import httplib2

from suds.transport import Reply
from suds.transport.http import HttpTransport
from suds.transport.http import HttpAuthenticated


class HttpTransportWithKeepAlive(HttpAuthenticated, object):

    def __init__(self):
        super(HttpTransportWithKeepAlive, self).__init__()
        self.http = httplib2.Http(timeout=20,
                                  disable_ssl_certificate_validation=True)

    def open(self, request):
        return HttpTransport.open(self, request)

    def send(self, request):
        headers_as_strings = {key: str(value) for (key, value) in request.headers.items()}

        headers, message = self.http.request(request.url, "POST",
                                             body=request.message,
                                             headers=headers_as_strings)
        response = Reply(200, headers, message)
        return response
