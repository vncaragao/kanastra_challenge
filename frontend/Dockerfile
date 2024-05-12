FROM node:18.18.0

ENV PORT 8888

RUN mkdir -p /usr/src/frontend
WORKDIR /usr/src/frontend

COPY ./frontend .

RUN npm install

EXPOSE 8888

CMD "npm" "run" "dev:node"
