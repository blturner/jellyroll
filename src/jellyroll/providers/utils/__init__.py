import httplib2
import json
import dateutil.parser
import dateutil.tz
from django.utils.encoding import force_unicode
from django.utils.timezone import utc
from django.conf import settings
from jellyroll.providers.utils.anyetree import etree

DEFAULT_HTTP_HEADERS = {
    "User-Agent" : "Jellyroll/1.0 (http://github.com/jacobian/jellyroll/tree/master)"
}

#
# URL fetching sugar
#
    
def getxml(url, **kwargs):
    """Fetch and parse some XML. Returns an ElementTree"""
    xml = fetch_resource(url, **kwargs)
    return etree.fromstring(xml)
    
def getjson(url, **kwargs):
    """Fetch and parse some JSON. Returns the deserialized JSON."""
    data = fetch_resource(url, **kwargs)
    return json.loads(data)

def fetch_resource(url, method="GET", body=None, username=None, password=None, headers=None):
    h = httplib2.Http(timeout=15, disable_ssl_certificate_validation=True)
    h.force_exception_to_status_code = True
    
    if username is not None or password is not None:
        h.add_credentials(username, password)
    
    if headers is None:
        headers = DEFAULT_HTTP_HEADERS.copy()
    
    response, content = h.request(url, method, body, headers)
    return content
    
#
# Date handling utils
#

def parsedate(s):
    """
    Convert a string into a UTC timezone aware datetime object if
    settings.USE_TZ is True. Otherwise returns a naive datetime.
    """
    if settings.USE_TZ:
        return dateutil.parser.parse(s).replace(tzinfo=utc)
    return dateutil.parser.parse(s).replace(tzinfo=None)

def safeint(s):
    """Always returns an int. Returns 0 on failure."""
    try:
        return int(force_unicode(s))
    except (ValueError, TypeError):
        return 0


JELLYROLL_ADJUST_DATETIME = False
if hasattr(settings,'JELLYROLL_ADJUST_DATETIME'):
    JELLYROLL_ADJUST_DATETIME = settings.JELLYROLL_ADJUST_DATETIME

if JELLYROLL_ADJUST_DATETIME:
    try:
        import pytz
    except ImportError:
        import logging
        log = logging.getLogger('jellyroll.providers.utils')
        log.error("Cannot import pytz package and consequently, all datetime objects will be naive. "
                  "In this particular case, e.g., all commit dates will be expressed in UTC.")

    import datetime
    import time

    UTC = pytz.timezone('UTC')
    LOCAL = pytz.timezone(settings.TIME_ZONE)

    def utc_to_local_datetime(dt):
        """
        Map datetime as UTC object to it's localtime counterpart.
        """
        return dt.astimezone(LOCAL)

    def utc_to_local_timestamp(ts, orig_tz=UTC):
        """
        Convert a timestamp object into a tz-aware datetime object.
        """
        timestamp = datetime.datetime.fromtimestamp(ts,tz=orig_tz)
        return timestamp.astimezone(LOCAL)

    def utc_to_local_timestruct(ts, orig_tz=UTC):
        """
        Convert a timestruct object into a tz-aware datetime object.
        """
        return utc_to_local_timestamp(time.mktime(ts),orig_tz)
