FROM python:3

WORKDIR /usr/src/app

RUN pip install 'strawberry-graphql[debug-server]'

CMD [ "strawberry", "server", "app" ]
