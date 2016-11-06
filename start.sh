#!/bin/sh
set -e
env > /tmp/env.var
exec lighttpd -D -f /etc/lighttpd/lighttpd.conf
