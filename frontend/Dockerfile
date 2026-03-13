FROM node:20-alpine

WORKDIR /app

COPY package.json tsconfig.json next.config.ts next-env.d.ts ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--hostname", "0.0.0.0"]
