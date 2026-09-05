#homwwork objectives 
#this project apart from only the image genration also tell the time taken for image to genrate using  time library 

# asks the user how much brightness and contrast they want 

import time 
from huggingface_hub import InferenceClient 
from datetime import datetime 
from PIL import Image , ImageEnhance, ImageFilter
import time 

HF_API_KEY="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"

MODELS = [
"ByteDance/SDXL-Lightning",
"stabilityai/stable-diffusion-xl-base-1.0",
"stabilityai/sdxl-turbo",
"runwayml/stable-diffusion-v1-5", 
]

client=InferenceClient(api_key=HF_API_KEY)

print(f"Primary model: {MODELS[0]}")
print("type 'quit' to exit\n")

while True:
    prompt=input("Enter promt: ").strip()

    if prompt.lower() in ["quit","exit","q"]:
        break

    start_time = time.perf_counter()

    if not prompt:
        continue 

    print("Genrating...")
    image=None

    for model in MODELS:
        try:
            image=client.text_to_image(prompt, model=model)
            break
        except Exception:
            print(f"Executing next...")
            continue

    if image:
        timestamp= datetime.now().strftime("%Y%m%d_%H%M%S")
        filename=f"generated_{timestamp}.png"
        image.save(filename)
        print(f"saved :{filename}")

        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"The code took {execution_time:.4f} seconds to complete.")

        image.show()
        time.sleep(5)

        brightness = float(input("How much should brightness be changed? (1.0 = same, >1 = increase, <1 = decrease): "))
        contrast = float(input("How much should contrast be changed? (1.0 = same, >1 = increase, <1 = decrease): "))

        image = ImageEnhance.Brightness(image).enhance(brightness)
        image = ImageEnhance.Contrast(image).enhance(contrast)

        image.show()
        print()

    else:
        print("Error all modl=els failed.Check your api key")

print("goodbye")