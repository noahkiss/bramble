FROM node:24-slim AS builder

RUN corepack enable pnpm

WORKDIR /app

COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
RUN pnpm install --frozen-lockfile

COPY . .
RUN pnpm build

FROM node:24-slim AS runtime

RUN corepack enable pnpm

WORKDIR /app

COPY --from=builder /app/build ./build
COPY --from=builder /app/package.json ./
COPY --from=builder /app/pnpm-lock.yaml ./
# This is a second, independent install, so it needs the allowBuilds list too.
# Nothing in the production tree runs an install script today, but pnpm 11
# defaults strictDepBuilds to true: the first native prod dependency added
# without this file turns a silent "Ignored build scripts" into a failed build.
COPY --from=builder /app/pnpm-workspace.yaml ./
RUN pnpm install --frozen-lockfile --prod

ENV NODE_ENV=production
ENV PORT=3000
ENV HOST=0.0.0.0

USER node

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "fetch('http://localhost:3000').then(r => r.ok ? process.exit(0) : process.exit(1)).catch(() => process.exit(1))"

CMD ["node", "build"]
