from fastapi import APIRouter, UploadFile, File, Form
from app.vision_ai import analyze_image_with_ai
from app.decision_engine import decide

router = APIRouter(
    tags=["Maize Analysis"]
)

@router.post("/analyze")
async def analyze(
    image: UploadFile = File(...),
    crop_stage: str = Form(...),
    plant_part: str = Form(...)
):
    image_bytes = await image.read()

    # 1. AI extracts visible symptoms ONLY
    ai_result = analyze_image_with_ai(image_bytes)
    symptoms = ai_result["visible_symptoms"]

    # 2. RULE ENGINE decides category + action
    decision = decide(symptoms, crop_stage, plant_part)

    # 3. Final structured response
    return {
        "crop": "Maize",
        "crop_stage": crop_stage,
        "plant_part": plant_part,
        "category": decision["category"],
        "primary_diagnosis": decision["diagnosis"],
        "confidence": decision["confidence"],
        "evidence": decision["evidence"],
        "recommended_actions": decision["actions"],
        "market_solutions": decision["market_solutions"],
        "risk_level": decision["risk"],
        "disclaimer": "Advisory only"
    }
