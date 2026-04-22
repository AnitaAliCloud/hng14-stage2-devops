# HNG14 Stage 2 DevOps — Job Processing System

A containerised job processing system with four services:

| Service | Tech | Description |
|---|---|---|
| frontend | Node.js | Submit jobs and track status |
| api | Python/FastAPI | Creates jobs and serves status |
| worker | Python | Processes jobs from the queue |
| redis | Redis 7 | Shared queue and job state store |

## Prerequisites

- Docker Desktop
- Git

## How to run from scratch

### 1. Clone the repo

```bash
git clone https://github.com/AnitaAliCloud/hng14-stage2-devops.git
cd hng14-stage2-devops
```

### 2. Create your .env file

```bash
cp .env.example .env
```

### 3. Start the stack

```bash
docker compose up --build
```

### 4. Open the app

Go to http://localhost:3000 in your browser

## What a successful startup looks like

Container hng14-stage2-devops-redis-1    Healthy
Container hng14-stage2-devops-api-1      Healthy
Container hng14-stage2-devops-worker-1   Healthy
Container hng14-stage2-devops-frontend-1 Healthy

## Architecture

Browser → Frontend :3000 → API :8000 → Redis
↑
Worker

## Bugs Fixed

See FIXES.md for every bug found and fixed.