import redis
import time
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    decode_responses=True
)


def process_job(job_id):
    logger.info(f"Processing job {job_id}")
    time.sleep(2)
    r.hset(f"job:{job_id}", "status", "completed")
    logger.info(f"Done: {job_id}")


while True:
    try:
        job = r.brpop("jobs", timeout=5)
        if job:
            _, job_id = job
            process_job(job_id)
    except Exception as e:
        logger.error(f"Worker error: {e}")
        time.sleep(2)

