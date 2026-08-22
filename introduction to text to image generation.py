from huggingface_hub import InferenceClient 
from datetime import datetime 
from PIL import Image , ImageEnhance, ImageFilter
import time 
HF_API_KEY="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"
MODELS = [
"ByteDance/SDXL-Lightning",
"stabilityai/stable-diffusion-xl-base-1.0",
"stabilityai/sdxl-turbo",
"runwayml/stable-diffusion-v1-5", # Fallback 2
]
client=InferenceClient(api_key=HF_API_KEY)
print(f"Primary model: {MODELS[0]}")
print("type 'quit' to exit\n")
while True:
    prompt=input("Enter promt: ").strip()
    if prompt.lower() in ["quit","exit","q"]:
        break
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
        image.show()
        time.sleep(5)
        image= ImageEnhance.Brightness(image).enhance(1.2)
        image= ImageEnhance.Contrast(image).enhance(1.3)
        image.show()
        print()
    else:
        print("Error all modl=els failed.Check your api key")
print("gooooooidbai")
