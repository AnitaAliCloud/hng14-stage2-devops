FROM node:20.19.1-slim AS builder

WORKDIR /build

COPY package*.json ./
RUN npm install --omit=dev

FROM node:20.19.1-slim

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

RUN groupadd --system appgroup && \
    useradd --system --gid appgroup appuser

WORKDIR /app

COPY --from=builder /build/node_modules ./node_modules
COPY --chown=appuser:appgroup . .

RUN rm -f .env

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=15s --timeout=5s --start-period=10s --retries=3 \
    CMD node -e "require('http').get('http://localhost:3000/health', r => process.exit(r.statusCode === 200 ? 0 : 1)).on('error', () => process.exit(1))"

CMD ["node", "app.js"]