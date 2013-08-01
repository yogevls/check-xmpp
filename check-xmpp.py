#!/usr/bin/env python

import sleekxmpp, argparse, sys, logging
from sleekxmpp import ClientXMPP

#
sleekxmpp.xmlstream.xmlstream.logging.disable('CRITICAL')

parser = argparse.ArgumentParser(description='XMPP Connectivity Test')
parser.add_argument('--host', default=None)
parser.add_argument('--port', default=5222)
args = parser.parse_args()

if args.host is None:
    print "Missing --host. Please type the command with hostname: \
           \n./check_xmpp.py --host acme.example.com"
    sys.exit()

c = ClientXMPP(None, None)
exit_code = 0

try:
    if c.connect(address=(args.host, args.port), reattempt=False, use_tls=False, use_ssl=False) is False:
        exit_code = 2
        print "%s-Connection to %s is Down" % (exit_code, args.host)
        sys.exit(exit_code)
    else:
        print "%s-Connection to %s is OK" % (exit_code, args.host)
        sys.exit(exit_code)
except Exception as e:
    exit_code = 3
    print "%s-Faild XMPP connectivity check to %s -" (exit_code, args.host, e)
    sys.exit(exit_code)