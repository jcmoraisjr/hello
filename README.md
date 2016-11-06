#Hello

A very small (10MiB uncompressed) image with Alpine Linux, TZ data, Lighttpd and Bash used to test deployments on clusters (Kubernetes) as well as standalone (Docker) container installations.

[![Docker Repository on Quay](https://quay.io/repository/jcmoraisjr/hello/status "Docker Repository on Quay")](https://quay.io/repository/jcmoraisjr/hello)

#So what

Container's hostname, timezone, remote address including X-Forwarded-For header (if provided), ip address and so on. All of them are provided in a single html page.

Nice for tests.

#Usage

Run:

    docker run -p 8080:8080 quay.io/jcmoraisjr/hello

View:

    http://localhost:8080

Environment variables are propagated:

    docker run -e TZ=Europe/Monaco -p 8080:8080 quay.io/jcmoraisjr/hello

Another env var?

    docker run -e VAR1='user agent:HTTP_USER_AGENT' -p 8080:8080 quay.io/jcmoraisjr/hello

Another command?

    docker run -e CMD1='env vars:env' -p 8080:8080 quay.io/jcmoraisjr/hello

More than one env var or command? Define `VAR2`, `VAR3`, `CMD2`, `CMD3`, ...
