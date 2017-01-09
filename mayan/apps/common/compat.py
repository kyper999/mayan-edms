from __future__ import unicode_literals

import sys

try:
    import urlparse  # Python 2.x
except ImportError:
    import urllib.parse as urlparse

if sys.version_info[0] == 3:
    from django.utils.encoding import smart_text as smart_unicode
else:
    from django.utils.encoding import smart_unicode

try:
    from cStringIO import StringIO
except ImportError:
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

try:
    from email.Utils import collapse_rfc2231_value
except ImportError:
    from email.utils import collapse_rfc2231_value

try:
    from urllib import unquote_plus
except ImportError:
    from urllib.parse import unquote_plus

