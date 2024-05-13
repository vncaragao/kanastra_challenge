FROM node:18.18.0

ENV PORT 80

RUN mkdir -p /usr/src/frontend
WORKDIR /usr/src/frontend

COPY ./frontend .

RUN npm install
RUN npm cache clean --force
RUN npm install vite @esbuild/linux-x64




EXPOSE 80/tcp

CMD ["npm", "run", "dev:node", "--host", "0.0.0.0"]
