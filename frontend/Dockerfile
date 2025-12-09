# frontend/Dockerfile
FROM node:20-alpine AS build

WORKDIR /app

# Копируем только package файлы для кэширования
COPY package.json package-lock.json* ./

# Устанавливаем зависимости (используем npm install вместо npm ci)
RUN npm install

# Копируем остальной код
COPY . .

# Собираем проект
RUN npm run build

# Production image
FROM nginx:alpine

# Копируем собранное приложение
COPY --from=build /app/dist /usr/share/nginx/html

# Копируем конфиг nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]