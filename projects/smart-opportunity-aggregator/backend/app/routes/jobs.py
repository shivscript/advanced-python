from fastapi import APIRouter

from app.database import jobs_collection
from app.scraper.job_scraper import scrape_jobs

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/scrape")
def scrape_and_store_jobs():
    jobs = scrape_jobs()
    if jobs:
        jobs_collection.insert_many(jobs)
    return {"message": "Jobs scraped and stored"}


@router.get("/")
def get_jobs():
    return list(jobs_collection.find({}, {"_id": 0}))
