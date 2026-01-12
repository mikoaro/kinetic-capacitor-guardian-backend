import base64
import sys
import io
from PIL import Image

def optimize_and_convert(image_path):
    """
    Resizes an image to max 640px width, compresses it as JPEG,
    and returns the Base64 string.
    """
    try:
        # 1. Open the image
        with Image.open(image_path) as img:
            
            # 2. Convert to RGB (in case of PNG with transparency)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # 3. Resize if too large (Max width 640px)
            max_width = 640
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                print(f"Resized image to: {max_width}x{new_height}")

            # 4. Save to byte buffer as JPEG
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG", quality=85)
            buffer_size = buffer.tell()
            
            # 5. Convert to Base64
            encoded_string = base64.b64encode(buffer.getvalue()).decode('utf-8')

            print(f"\n--- OPTIMIZED SUCCESS ---")
            print(f"Original Size: {buffer_size / 1024:.2f} KB")
            print("\n--- COPY THE CONTENT BELOW ---")
            print(encoded_string)
            print("--- END OF CONTENT ---\n")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python optimize_and_convert.py <path_to_image>")
    else:
        optimize_and_convert(sys.argv[1])