from PIL import Image, ImageDraw
import streamlit as st

def crop_to_circle(image_path, center=None, radius=None):
    # Open the image
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size

    # Default to center of the image
    if center is None:
        center = (width*1.006 // 2, height*1.1 // 2)

    # Default radius
    if radius is None:
        radius = min(width, height) // 2

    # Create a circular mask
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse(
        (center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius),
        fill=255,
    )

    # Apply the mask to the image
    result = Image.new("RGBA", (width, height), (255, 255, 255, 0))  # Transparent background
    result.paste(img, (0, 0), mask=mask)

    # Crop the result to the circle's bounding box
    result = result.crop(
        (
            center[0] - radius,
            center[1] - radius,
            center[0] + radius,
            center[1] + radius,
        )
    )

    return result


