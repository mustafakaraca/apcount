#!/usr/bin/env python

import sys, getopt
import redis

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "lh:p:", ["list", "host=", "port="])
  except getopt.GetoptError:
    print('clilist.py [-l | --list] [-h <host>| --host=<host>] [-p <port> | --port=<port>]')
    sys.exit(2)
  host = '127.0.0.1'
  port = 17001 
  dolist = False
  for opt, arg in opts:
    if opt in ('-l', '--list'):
      dolist = True
    elif opt in ('-h', '--host'):
      host = str(arg)
    elif opt in ('-p', '--port'):
      port = int(arg)
  rd = redis.StrictRedis(host=host, port=port)
  setlist = rd.scan_iter('pingtimer:{*}')
  if dolist:
    for n in setlist:
      for d in rd.zrange(n, 0, -1):
        print(d)
  else:
    print(sum([rd.zcard(t) for t in setlist]))

if __name__ == "__main__":
  main(sys.argv[1:])
