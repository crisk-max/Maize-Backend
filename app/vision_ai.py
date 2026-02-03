from io import BytesIO
from statistics import mean, pstdev

from PIL import Image


def _summarize_colors(image):
    resized = image.convert("RGB").resize((128, 128))
    pixels = list(resized.getdata())
    reds = [pixel[0] for pixel in pixels]
    greens = [pixel[1] for pixel in pixels]
    blues = [pixel[2] for pixel in pixels]
    avg_red = mean(reds)
    avg_green = mean(greens)
    avg_blue = mean(blues)
    luminance_values = [
        0.2126 * r + 0.7152 * g + 0.0722 * b for r, g, b in pixels
    ]
    brightness = mean(luminance_values)
    contrast = pstdev(luminance_values)
    return avg_red, avg_green, avg_blue, brightness, contrast


def analyze_image_with_ai(image_bytes):
    try:
        image = Image.open(BytesIO(image_bytes))
    except OSError:
        return {
            "visible_symptoms": ["image unreadable or unsupported format"],
            "confidence": 0.1
        }

    avg_red, avg_green, avg_blue, brightness, contrast = _summarize_colors(image)

    symptoms = []
    if avg_green > avg_red * 1.1 and avg_green > avg_blue * 1.1:
        symptoms.append("dominant green foliage")
    if avg_red > avg_green * 1.1 and avg_blue > avg_green * 1.1:
        symptoms.append("purple or reddish pigmentation")
    if avg_red > avg_blue * 1.1 and avg_green > avg_blue * 1.1 and brightness > 120:
        symptoms.append("yellowing or chlorosis")
    if brightness < 90 and contrast > 25:
        symptoms.append("possible lesions or necrosis")

    if not symptoms:
        symptoms.append("no clear visual stress indicators")

    confidence = 0.55
    if len(symptoms) >= 2:
        confidence = 0.7
    if "image unreadable or unsupported format" in symptoms:
        confidence = 0.1

    return {
        "visible_symptoms": symptoms,
        "confidence": confidence
    }
