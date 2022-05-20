import os
from fastapi import FastAPI, APIRouter, HTTPException, status
from typing import List
import motor.motor_asyncio
from job_terms_backend.models import Term

term_router = APIRouter(tags=["Term"], prefix="/terms")
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
db = client.jobTerm


@term_router.get(
    "/", response_description="List all terms", response_model=List[Term]
)
async def list_terms():
    terms = await db["term"].find().to_list()
    return terms


@term_router.get(
    "/random", response_description="Get a random term", response_model=Term
)
async def show_random_term():
    if term_cursor := db["term"].aggregate([{"$sample": {"size": 1}}]):
        async for term in term_cursor:
            db.term.update_one(
                {'name': term["name"]},
                {"$inc": {'views': 1}})
            return term

    raise HTTPException(status_code=404, detail=f"Term not found")


@term_router.get(
    "/{name}", response_description="Get a single term", response_model=Term
)
async def show_term(name: str):
    if (term := await db["term"].find_one({"name": name})) is not None:
        db.term.update_one(
            {'name': name},
            {"$inc": {'views': 1}})
        return term

    raise HTTPException(status_code=404, detail=f"Term '{name}' not found")


@term_router.patch(
    "/{name}/like", response_description="Like a term"
)
async def like_term(name: str):
    if (await db["term"].find_one({"name": name})) is not None:
        await db.term.update_one(
                {'name': name},
                {"$inc": {'like': 1}})

        like_counter = await db["term"].find_one({"name": name})
        return {"like": like_counter["like"]}

    raise HTTPException(status_code=404, detail=f"Term '{name}' not found")


@term_router.patch(
    "/{name}/dislike", response_description="Dislike a term"
)
async def dislike_term(name: str):
    if (await db["term"].find_one({"name": name})) is not None:
        await db.term.update_one(
                {'name': name},
                {"$inc": {'dislikes': 1}})

        dislike_counter = await db["term"].find_one({"name": name})
        return {"dislikes": dislike_counter["dislikes"]}

    raise HTTPException(status_code=404, detail=f"Term '{name}' not found")