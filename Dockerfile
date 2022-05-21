FROM alpine:latest
RUN apk add --no-cache python3 py3-pip
RUN apk add --no-cache gcc make cmake
RUN apk add --no-cache git gnupg wget curl
RUN apk add --no-cache rsync ssh-audit
RUN apk add --no-cache npm ruby ruby-dev
RUN apk add --no-cache elinks
#RUN gem install rdoc timetrap
RUN apk add hping3 --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing hping3
RUN mkdir /menu
RUN chmod a+r /menu
COPY menu.py /menu/menu.py
RUN chmod a+x /menu/menu.py
ENTRYPOINT ["/menu/menu.py"]