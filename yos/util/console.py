# Copyright (c) 2008 Yahoo! Inc. All rights reserved.
# Licensed under the Yahoo! Search BOSS Terms of Use
# (http://info.yahoo.com/legal/us/yahoo/search/bosstos/bosstos-2317.html)

__author__ = "Vik Singh (viksi@yahoo-inc.com)"

def strfix(msg):
  """
  Copies this recipe: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/523011
  Constants out any characters that spew encoding errors
  """
  goodchars = {}
  try:
    return str(msg)
  except UnicodeEncodeError:
    res=''
    for i in list(msg):
      if i not in goodchars:
        try:
          str(i)
          goodchars[i] = i
        except UnicodeEncodeError:
          # format character as python string constant
          code = ord(i)
          t = None
          if code < 256:
            t ='\\x%02x' % code # 8-bit value
          elif code < 65536:
            t ='\\u%04x' % code # 16-bit value unicode
          else:
            t = '\\U%08x' % code # other values as 32-bit unicode
          goodchars[i] = t # or '.' for readability ;-)
      res += goodchars[i]
    return res

def write(msg):
  print strfix(msg)
