FROM alpine:3.4
RUN apk add --no-cache tzdata bash lighttpd

COPY lighttpd.conf /etc/lighttpd/
COPY index.cgi /var/www/localhost/htdocs/
COPY start.sh /
RUN chmod +x /var/www/localhost/htdocs/index.cgi /start.sh\
 && chown lighttpd:lighttpd /run

USER lighttpd
CMD ["/start.sh"]
