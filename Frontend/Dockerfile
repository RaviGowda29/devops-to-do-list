# Use Node 18 as the base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package files first (for Docker caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of your app
COPY . .

# Build the Next.js app
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
