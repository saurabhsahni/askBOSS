#Copyright (c) 2011 Yahoo! Inc. All rights reserved. Licensed under the BSD License. 
# See accompanying LICENSE file or http://www.opensource.org/licenses/BSD-3-Clause for the specific language governing permissions and limitations under the License.


"""
This is the Boss search API
search is the main function

Examples:
  web_results = search("britney spears")
  news_20_results = search("tiger woods", vertical="news", count=20)
"""

__author__ = "BOSS Team"

from urllib import quote_plus

import oauth
import time
import urllib,urllib2
import simplejson
import logging

from yos.crawl import rest

CONFIG = simplejson.load(open("config", "r"))
SEARCH_API_URL_V1 = CONFIG["uri_v1"].rstrip("/") + "/%s/v%d/%s?start=%d&count=%d&lang=%s&region=%s" + "&appid=" + CONFIG["appid"]
SEARCH_API_URL_V2 = CONFIG["uri_v2"]
CC_KEY = CONFIG['cc_key']
CC_SECRET = CONFIG['cc_secret']
SOURCE_TAG = ""

def params(d):
  """ Takes a dictionary of key, value pairs and generates a cgi parameter/argument string """
  p = ""
  for k, v in d.iteritems():
    p += "&%s=%s" % (quote_plus(k), quote_plus(v))
  return p

def search(command,vertical="web",count=10,start=0,more={}):
  params = {
     'oauth_version': "1.0",
     'oauth_nonce': oauth.generate_nonce(),
     'oauth_timestamp': int(time.time()),
     'q': quote_plus(command),
     'count': count,
     'start': start,
     'format': 'json',
     'ads.recentSource': SOURCE_TAG 
  }
  params.update(more)
  url =  SEARCH_API_URL_V2 + vertical
  consumer = oauth.OAuthConsumer(CC_KEY,CC_SECRET)
  req = oauth.OAuthRequest.from_consumer_and_token(consumer,http_method="GET", http_url=url, parameters=params)
  signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1()
  req.sign_request(signature_method, consumer, None)
  resp=req.to_url()
  return rest.load_json(resp) 

def search_v1(command, vertical="web", version=1, start=0, count=10, lang="en", region="us", more={}):
  """
  command is the query (not escaped)
  vertical can be web, news, spelling, images
  lang/region default to en/us - take a look at the the YDN Boss documentation for the supported lang/region values
  """
  url = SEARCH_API_URL_V1 % (vertical, version, quote_plus(command), start, count, lang, region) + params(more)
  return rest.load_json(url)