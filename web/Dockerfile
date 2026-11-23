# web container (D1): the React build served by Node.js + Express. Build context: the repository root.

# 1. Build the React page with Vite. config/personal-data.json is shared with the RAG service (D3).
FROM node:24.22.2-alpine AS build
WORKDIR /repo
COPY config/personal-data.json config/personal-data.json
COPY web/client/package.json web/client/package-lock.json* web/client/
RUN cd web/client && (npm ci || npm install)
COPY web/client web/client
RUN cd web/client && npm run build

# 2. The web backend with only its runtime packages.
FROM node:24.22.2-alpine
ENV NODE_ENV=production PORT=3000
WORKDIR /app
# --chown and chmod: the files must be readable by the node user, whatever their permissions on the host.
COPY --chown=node:node web/server/package.json web/server/package-lock.json* ./
RUN npm ci --omit=dev || npm install --omit=dev
COPY --chown=node:node web/server/index.js ./
COPY --from=build --chown=node:node /repo/web/client/dist ./public
RUN chmod -R a+rX /app
USER node
EXPOSE 3000
CMD ["node", "index.js"]
