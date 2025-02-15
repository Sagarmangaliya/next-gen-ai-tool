from PIL import Image

def process_image(file):
    # Replace with your custom image processing logic
    image = Image.open(file.file)
    return f"Processed image: {image.size}"
