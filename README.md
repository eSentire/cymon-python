# cymon-python
Python library for Cymon.io APIs

Example:  
```
from cymon import Cymon
api=cymon('YOUR KEY GOES HERE')
api.ip_events(8.8.8.8)
```
Output:
```
{u'updated': u'2015-05-21T19:21:29', u'addr': u'8.8.8.8', u'created': u'2015-03-23T12:03:42', u'timeline': u'https://cymon.io/api/nexus/v1/ip/8.8.8.8/timeline', u'sources': [u'malwr.com', u'virustotal.com', u'urlquery.net', u'google safebrowsing'], u'urls': u'https://cymon.io/api/nexus/v1/ip/8.8.8.8/urls', u'domains': u'https://cymon.io/api/nexus/v1/ip/8.8.8.8/domains', u'events': u'https://cymon.io/api/nexus/v1/ip/8.8.8.8/events'}
```
