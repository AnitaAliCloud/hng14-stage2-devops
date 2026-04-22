# FIXES.md

## FIX-001
- **File:** `api/main.py`
- **Line:** 8
- **Problem:** Redis hardcoded to `localhost` — fails inside Docker
- **Fix:** Changed to use `os.environ.get("REDIS_HOST", "redis")`

## FIX-002
- **File:** `api/main.py`
- **Line:** 9
- **Problem:** Missing `/health` endpoint — Docker health checks return 404
- **Fix:** Added `GET /health` route returning `{"status": "ok"}`

## FIX-003
- **File:** `api/main.py`
- **Line:** 12
- **Problem:** Queue named `"job"` but worker listens on `"jobs"`
- **Fix:** Changed `r.lpush("job", ...)` to `r.lpush("jobs", ...)`

## FIX-004
- **File:** `api/main.py`
- **Line:** 19
- **Problem:** Missing job returns HTTP 200 with error message instead of proper 404
- **Fix:** Replaced with `raise HTTPException(status_code=404, detail="Job not found")`

## FIX-005
- **File:** `api/requirements.txt`
- **Line:** 1-3
- **Problem:** Dependencies have no version numbers — builds are not reproducible
- **Fix:** Pinned to `fastapi==0.111.0`, `uvicorn==0.29.0`, `redis==5.0.4`

## FIX-006
- **File:** `api/.env`
- **Line:** 1
- **Problem:** Real password `supersecretpassword123` committed to git history
- **Fix:** Removed from git tracking, wiped from history with `git filter-branch`, added `.env` to `.gitignore`

## FIX-007
- **File:** `worker/worker.py`
- **Line:** 6
- **Problem:** Redis hardcoded to `localhost` — fails inside Docker
- **Fix:** Changed to use `os.environ.get("REDIS_HOST", "redis")`

## FIX-008
- **File:** `worker/worker.py`
- **Line:** 13
- **Problem:** Worker listens on queue `"job"` but API pushes to `"jobs"`
- **Fix:** Changed `r.brpop("job", ...)` to `r.brpop("jobs", ...)`

## FIX-009
- **File:** `worker/worker.py`
- **Line:** 13-16
- **Problem:** No error handling — worker crashes silently on any failure
- **Fix:** Wrapped loop in `try/except` with proper logging

## FIX-010
- **File:** `worker/worker.py`
- **Line:** 4
- **Problem:** `signal` imported but never used — fails linter
- **Fix:** Removed unused import

## FIX-011
- **File:** `worker/requirements.txt`
- **Line:** 1
- **Problem:** No version number on redis dependency
- **Fix:** Pinned to `redis==5.0.4`

## FIX-012
- **File:** `frontend/app.js`
- **Line:** 6
- **Problem:** API URL hardcoded as `http://localhost:8000` — fails inside Docker
- **Fix:** Changed to `process.env.API_URL || "http://api:8000"`

## FIX-013
- **File:** `frontend/app.js`
- **Line:** N/A
- **Problem:** Missing `/health` endpoint — Docker health checks fail
- **Fix:** Added `GET /health` route returning `{"status": "ok"}`

## FIX-014
- **File:** `frontend/package.json`
- **Line:** 10-11
- **Problem:** `^` prefix on versions allows unpredictable updates
- **Fix:** Removed `^` to pin exact versions

## FIX-015
- **File:** `README.md`
- **Line:** N/A
- **Problem:** README is empty — no setup instructions
- **Fix:** Replaced with full setup guide