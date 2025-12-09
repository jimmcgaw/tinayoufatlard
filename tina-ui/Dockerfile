# Use an official Node.js runtime as a parent image
FROM node:25-alpine

# Set working directory inside the container
WORKDIR /app

# Install dependencies first (leverages Docker layer caching)
COPY package.json package-lock.json* ./
RUN npm ci

# Copy the rest of the application code
COPY . .

# Build the Next.js app (this will also compile TypeScript)
RUN npm run build

# Set environment to production
ENV NODE_ENV=development
ENV PORT=3000

# Expose the port Next.js listens on
EXPOSE 3000

# Start the app (make sure "start" runs "next start" in package.json)
CMD ["npm", "start"]
