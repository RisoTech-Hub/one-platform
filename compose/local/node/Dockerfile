FROM node:16-bullseye-slim

WORKDIR /app

COPY ./package.json /app

RUN npm install yarn

RUN yarn install && yarn cache clean --force

ENV PATH ./node_modules/.bin/:$PATH
