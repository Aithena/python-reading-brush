# -*- coding: utf-8 -*-
# ==================================================
# 对 Timer 做以下再封装的目的是：当某个功能需要每隔一段时间被
# 执行一次的时候，不需要在回调函数里对 Timer 做重新安装启动
# ==================================================
__author__ = 'liqingyun'

import urllib.request
from threading import Timer
from datetime import datetime

class MyTimer( object ):
  def __init__( self, start_time, interval, callback_proc, args=None, kwargs=None ):
    self.__timer = None
    self.__start_time = start_time
    self.__interval = interval
    self.__callback_pro = callback_proc
    self.__args = args if args is not None else []
    self.__kwargs = kwargs if kwargs is not None else {}

  def exec_callback( self, args=None, kwargs=None ):
    self.__callback_pro( *self.__args, **self.__kwargs )
    self.__timer = Timer( self.__interval, self.exec_callback )
    self.__timer.start()

  def start( self ):
    interval = self.__interval - ( datetime.now().timestamp() - self.__start_time.timestamp() )
    print( interval )
    self.__timer = Timer( interval, self.exec_callback )
    self.__timer.start()

  def cancel( self ):
    self.__timer.cancel() 
    self.__timer = None

class AI:
  def hello( self, name, age ):
    print( "[%s]\thello %s: %d\n" % (datetime.now().strftime("%Y%m%d %H:%M:%S"), name, age))

  def readHtml(self, name):
    url = 'http://dzwz7.ncms5.hnjing.net/case/69.html'
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    req = urllib.request.Request(url = url, headers = headers)
    resp = urllib.request.urlopen(req, timeout = 1000)
    html = resp.read()
    print("[%s] This is %s, Complete a browse." % (datetime.now().strftime("%Y%m%d %H:%M:%S"), name))

if __name__ == "__main__":

  xiaoyou = AI()
  start = datetime.now().replace( minute=3, second=0, microsecond=0 )
  # tmr = MyTimer( start, 60*60, xiaoyou.hello, [ "owenliu", 18 ] )
  tmr = MyTimer(start, 0.001*60, xiaoyou.readHtml, [ "xiaoyou"])
  tmr.start()