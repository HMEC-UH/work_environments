import os
import subprocess
from pdf2image import convert_from_path

# 1. Config Configurations
PPTX_FILE = "your-presentation.pptx"  # <-- Put your file name here
IMAGE_DIR = "docs/assets/images"       # <-- Your MkDocs image folder
MD_FILE = "docs/slides.md"             # <-- Where you want the markdown page

os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(os.path.dirname(MD_FILE), exist_ok=True)

# 2. Convert PPTX to PDF using headless LibreOffice (native on Linux)
print("Converting presentation to PDF via LibreOffice...")
subprocess.run([
    "libreoffice", "--headless", "--convert-to", "pdf", PPTX_FILE
], check=True)

pdf_filename = PPTX_FILE.replace(".pptx", ".pdf")

# 3. Convert PDF pages into clean high-res JPEG images
print("Rendering slide images...")
images = convert_from_path(pdf_filename, dpi=150)

# 4. Save images and write the clean Markdown file sequentially
print("Generating Markdown file...")
with open(MD_FILE, "w") as md:
    md.write(f"# {PPTX_FILE.replace('.pptx', '')}\n\n")
    
    for i, img in enumerate(images):
        slide_num = i + 1
        img_name = f"slide_{slide_num:02d}.jpg"
        img_path = os.path.join(IMAGE_DIR, img_name)
        
        # Save the crisp image file
        img.save(img_path, "JPEG")
        
        # Write clean markdown linking that specific slide
        md.write(f"### Slide {slide_num}\n")
        # Relative path from your docs directory for MkDocs
        md.write(f"![Slide {slide_num}](assets/images/{img_name})\n\n")
        md.write("---\n\n")

# Clean up the intermediate PDF file
if os.path.exists(pdf_filename):
    os.remove(pdf_filename)

print(f"🎉 Success! Your clean website page is ready at: {MD_FILE}")
