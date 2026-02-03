def decide(symptoms, crop_stage, plant_part):
    symptoms_text = " ".join(symptoms).lower()

    # 1. Disease — STRICT RULE
    if any(word in symptoms_text for word in ["lesion", "pustule", "rot", "mold", "blight"]):
        return {
            "category": "Disease",
            "diagnosis": "Disease symptoms detected",
            "confidence": 0.85,
            "evidence": symptoms,
            "actions": [
                "Confirm disease with field agronomist",
                "Follow integrated disease management practices"
            ],
            "market_solutions": [
                {
                    "type": "Fungicide",
                    "examples": [
                        "Protectant fungicides (e.g., chlorothalonil)",
                        "Systemic fungicides (e.g., triazoles)"
                    ],
                    "notes": "Select based on label for maize disease and rotate modes of action."
                },
                {
                    "type": "Biological control",
                    "examples": ["Trichoderma-based products", "Bacillus-based products"],
                    "notes": "Use as part of integrated disease management."
                },
                {
                    "type": "Cultural practices",
                    "examples": ["Remove infected residues", "Improve field airflow"],
                    "notes": "Reduces inoculum and disease pressure."
                }
            ],
            "risk": "High"
        }

    # 2. Pest damage — STRICT RULE
    if any(word in symptoms_text for word in ["chewing", "holes", "frass", "dead heart"]):
        return {
            "category": "Pest Damage",
            "diagnosis": "Insect damage detected",
            "confidence": 0.85,
            "evidence": symptoms,
            "actions": [
                "Inspect whorl and stem for pests",
                "Apply IPM practices if infestation confirmed"
            ],
            "market_solutions": [
                {
                    "type": "Insecticide",
                    "examples": ["Pyrethroids", "Diamides"],
                    "notes": "Use only after scouting confirms threshold levels."
                },
                {
                    "type": "Biopesticide",
                    "examples": ["Bacillus thuringiensis (Bt)", "Neem-based products"],
                    "notes": "Prefer early application for better efficacy."
                },
                {
                    "type": "Mechanical / trapping",
                    "examples": ["Pheromone traps", "Light traps"],
                    "notes": "Use for monitoring and suppression."
                }
            ],
            "risk": "High"
        }

    # 3. Nutrient deficiency / physiological stress
    if any(word in symptoms_text for word in ["purple", "yellow", "pale", "discoloration"]):
        return {
            "category": "Nutrient / Physiological Stress",
            "diagnosis": "Likely phosphorus deficiency or temperature-related stress",
            "confidence": 0.75,
            "evidence": symptoms,
            "actions": [
                "Check soil nutrient status",
                "Avoid unnecessary pesticide sprays",
                "Stress often reduces as crop establishes"
            ],
            "market_solutions": [
                {
                    "type": "Fertilizer",
                    "examples": ["DAP or MAP for phosphorus", "Balanced NPK"],
                    "notes": "Base rates on soil test results."
                },
                {
                    "type": "Foliar nutrition",
                    "examples": ["Foliar phosphorus blends", "Micronutrient mixes"],
                    "notes": "Use to correct short-term deficiencies."
                }
            ],
            "risk": "Low"
        }

    # 4. Healthy
    return {
        "category": "Healthy",
        "diagnosis": "No visible stress symptoms",
        "confidence": 0.9,
        "evidence": symptoms,
        "actions": [
            "Continue recommended agronomic practices"
        ],
        "market_solutions": [
            {
                "type": "Preventive care",
                "examples": ["Seed treatment where applicable", "Routine scouting"],
                "notes": "Focus on prevention rather than reactive spraying."
            }
        ],
        "risk": "None"
    }
