# cymon-python
Python library for [Cymon.io](https://cymon.io/) APIs

## Install

```
pip install cymon
```

## Example

```
from cymon import Cymon
api = Cymon()
api.ip_events('185.27.134.165')
```

## Output

```  
{u'count': 4,
 u'next': None,
 u'previous': None,
 u'results': [{u'created': u'2015-07-03T19:16:40',
   u'description': u'Posted: 2015-07-03 21:16:07\nIDS Alerts: 0\nURLQuery Alerts: 1\nBlacklists: 0\nMalicious page URL: hxxp://hostingpl.base.pk/aol.php',
   u'details_url': u'http://urlquery.net/report.php?id=1435950967981',
   u'tag': u'malicious activity',
   u'title': u'Malicious activity reported by urlquery.net',
   u'updated': u'2015-07-03T19:16:40'},
  {u'created': u'2015-03-01T18:11:19',
   u'description': None,
   u'details_url': None,
   u'tag': u'malware',
   u'title': u'Malware reported by Google SafeBrowsing',
   u'updated': u'2015-03-01T18:11:19'},
  {u'created': u'2015-02-28T19:48:16',
   u'description': None,
   u'details_url': u'http://app.webinspector.com/public/reports/show_website?result=2&site=http%3A%2F%2Fbymert1903.0fees.us',
   u'tag': u'malicious activity',
   u'title': u'Malicious website reported by app.webinspector.com',
   u'updated': u'2015-02-28T19:48:16'},
  {u'created': u'2015-02-23T14:32:10',
   u'description': None,
   u'details_url': None,
   u'tag': u'malware',
   u'title': u'Malware reported by AlienVault Reputation System',
   u'updated': u'2015-02-23T14:32:10'}]}
```

## Available methods

+ ip_lookup('x.x.x.x')
+ ip_events('x.x.x.x')
+ ip_domains('x.x.x.x')
+ ip_urls('x.x.x.x')
+ ip_timeline('x.x.x.x')
+ ip_blacklist(tag='malware')
+ domain_lookup()
+ url_lookup()