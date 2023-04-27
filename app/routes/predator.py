from fastapi import APIRouter
from app.services.predator import Predator as PredatorService
router = APIRouter()

@router.get("/predators")
async def get_predators():
    predators = await PredatorService.get_all_predators()
    return predators