FROM node:lts AS build
ADD . /app
WORKDIR /app
RUN npm install
RUN npm run build
