from django.utils.deprecation import MiddlewareMixin
from ipware import get_client_ip

# Need ipinfo signature
import ipinfo

__version__ = '0.1.0'

class IPInfoMiddleware(MiddlewareMixin):

    def process_request(self, request):
        ip_address, _ = get_client_ip(request)
        request._messages = default_storage(request)
        if ip_address:
            # Need config details
            ipinfo_client = ipinfo.getClient()
            request.ipinfo = ipinfo_client.getDetails(ip_address)
        else:
            request.ipinfo = None
