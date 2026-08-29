import os
import glob
import base64
from openai import OpenAI
from pydantic import BaseModel

# Initialize OpenAI client (it automatically looks for your OPENAI_API_KEY env variable)
client = OpenAI()

IMAGE_DIR = "docs/assets/images"
MD_FILE = "docs/slides.md"

# 1. Define the exact JSON structure we want ChatGPT to return
class SlideNarration(BaseModel):
    slide_number: int
    slide_title: str
    script: str

# Helper to encode local images to base64 strings for the Vision API
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Get all slide images sorted sequentially (slide_01.jpg, slide_02.jpg...)
slide_images = sorted(glob.glob(os.path.join(IMAGE_DIR, "slide_*.jpg")))

print(f"Found {len(slide_images)} slides. Beginning AI script writing...")

# Prepare to overwrite your markdown file with images + narration scripts
with open(MD_FILE, "w") as md:
    md.write("# Ocean Thermal Energy Conversion (OTEC) Presentation\n\n")

    for img_path in slide_images:
        base64_image = encode_image(img_path)
        filename = os.path.basename(img_path)
        
        # Extract the slide number from the filename (e.g., slide_12.jpg -> 12)
        current_num = int("".join(filter(str.isdigit, filename)))
        print(f"--> Processing Slide {current_num}...")

        try:
            # Call ChatGPT with vision and enforce our structural template format
            response = client.beta.chat.completions.parse(
                model="gpt-4o",
                response_format=SlideNarration, # Force response into our class schema
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": (
                                    "Act as an engineering professor giving a live presentation. "
                                    "Look closely at this slide graphic and write a natural spoken-word "
                                    "narration script. If there is a thermodynamic cycle loop, diagram, "
                                    "or chart, explain it fluidly to the audience rather than just listing text labels."
                                )
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ]
            )

            # Extract the automatically validated structured output object
            ai_data = response.choices[0].message.parsed
            
            # 2. Append the slide visual and the matching narrative directly to MkDocs
            md.write(f"### Slide {ai_data.slide_number}: {ai_data.slide_title}\n\n")
            
            # Material for MkDocs split grid layout (Visual Left, Text Right)
            md.write('<div class="grid cards" markdown>\n\n')
            md.write(f"-   ![{ai_data.slide_title}](assets/images/{filename})\n")
            md.write("-   #### Lecture Script\n")
            # Encase in a clean blockquote block
            md.write(f"    > \"{ai_data.script}\"\n\n")
            md.write("</div>\n\n")
            md.write("---\n\n")

        except Exception as e:
            print(f"❌ Error processing slide {current_num}: {e}")

print(f"🎉 Complete! Beautiful lecture page generated at: {MD_FILE}")
