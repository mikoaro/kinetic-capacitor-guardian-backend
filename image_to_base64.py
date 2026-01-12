import base64
import os
import sys

def convert_image_to_base64(image_path):
    """
    Reads an image file and converts it to a Base64 string.
    """
    # Check if file exists
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' was not found.")
        return

    # Read binary file
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Print the result
    print("\n--- COPY THE CONTENT BELOW ---")
    print(encoded_string)
    print("--- END OF CONTENT ---\n")
    print(f"Success! Character count: {len(encoded_string)}")

if __name__ == "__main__":
    # Usage check
    if len(sys.argv) < 2:
        print("Usage: python image_to_base64.py <path_to_image_file>")
        print("Example: python image_to_base64.py smoke_simulation.jpg")
    else:
        convert_image_to_base64(sys.argv[1])