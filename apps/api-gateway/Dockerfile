FROM node:20-alpine AS builder

WORKDIR /app

RUN corepack enable && corepack prepare pnpm@8.15.4 --activate

COPY package.json pnpm-workspace.yaml turbo.json ./
COPY apps/api-gateway ./apps/api-gateway
COPY packages/shared-types ./packages/shared-types

RUN pnpm install --frozen-lockfile
RUN pnpm --filter api-gateway build

FROM node:20-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production

COPY --from=builder /app/apps/api-gateway/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/apps/api-gateway/package.json ./package.json

EXPOSE 4000

CMD ["node", "dist/main"]
