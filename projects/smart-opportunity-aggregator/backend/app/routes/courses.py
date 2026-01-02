from fastapi import APIRouter

from app.database import courses_collection
from app.scraper.course_scraper import scrape_courses

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("/scrape")
def scrape_and_store_courses():
    courses = scrape_courses()
    if courses:
        courses_collection.insert_many(courses)
    return {"message": "Courses scraped and stored"}


@router.get("/")
def get_courses():
    return list(courses_collection.find({}, {"_id": 0}))
