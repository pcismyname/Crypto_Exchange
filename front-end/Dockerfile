FROM node:alpine

WORKDIR /app
COPY package.json ./
RUN npm install

COPY . .
# RUN npm run build
RUN npm run dev

# CMD ["npm", "build"]

EXPOSE 5173
