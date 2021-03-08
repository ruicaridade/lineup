FROM node:14-slim

COPY . /app
WORKDIR /app

RUN yarn install
RUN yarn build

# To keep this simple we're using react's built-in server, terrible, I know! I would instead mount a virtual volume
# on /app/build, and then serve with nginx as a separate service.
CMD ["yarn", "start"]
