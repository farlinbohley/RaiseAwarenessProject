from PIL import Image, ImageOps
import os

images = ["QField.png", "QGIS.png", "OrganicMaps.jpg", "Alicloud.avif"]
size = (1200, 628)

for img_name in images:
    if not os.path.exists(img_name):
        continue
    img = Image.open(img_name)
    # Convert RGBA to RGB for JPEG compatibility just in case but here we'll save in current format
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    # This automatically crops the image to fit the aspect ratio and scales it.
    img_cropped = ImageOps.fit(img, size, Image.Resampling.LANCZOS, centering=(0.5, 0.5))
    img_cropped.save(img_name)
    print(f"Resized and cropped {img_name}")

