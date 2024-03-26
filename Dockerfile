# Use a lightweight Node.js image as the base
FROM node:alpine

# Create a working directory inside the image
WORKDIR /app

# Copy necessary dependency files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of your React project files
COPY . .

# Build your React app for production
RUN npm run build

# Use a webserver (like NGINX) to serve your built app
FROM nginx:alpine

# Copy the built React app into the NGINX serving directory
COPY --from=0 /app/build /usr/share/nginx/html

# Expose the port NGINX listens on
EXPOSE 80

# Start NGINX when the container starts
CMD ["nginx", "-g", "daemon off;"]
