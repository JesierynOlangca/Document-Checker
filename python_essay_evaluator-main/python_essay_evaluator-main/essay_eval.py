import base64
import requests
import json
import sys

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"  # Change if you're using a different name

def encode_image_to_base64(image_path):
    """Encodes an image file to base64 string."""
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded

def query_gemma3_vision(image_path1, prompt=\
    "Evaluate the attached document based on the following expectations: \
    1. Mastery of fundamental knowledge in the field.\
    2. Ability to access and integrate information into a cohesive overview of current knowledge; ability to critically evaluate the meaning, value, and contribution of published literature in the field.\
    3. Imagination and originality of thought\
    4. Ability to design and implement an appropriate collection and analysis of data or ability to articulate a critical response to dramatic or artistic theory, literature, design and performance in one's own work or that of another artist\
    5. Ability to draw reasoned conclusions from a body of knowledge\
    6. Impact of research on the field\
    Use the rubric below to give a score:\
    Exceptional (4): The Capstone Project demonstrates a strong grasp of both foundational and advanced concepts, applying them creatively to an original and impactful topic with innovative outcomes. Data interpretation and critical analysis are executed with sophistication, yielding conclusions that are both relevant and highly contributive to the field.\
    Strong (3): The Capstone Project frequently integrates fundamental and some advanced concepts, showing a good understanding of relevant literature and an original approach to the study’s purpose and design. Data interpretation is mostly appropriate with some critical insight, and the conclusions are valid and contribute meaningfully—though not profoundly—to the field.\
    Marginal (2): The Capstone Project shows a moderate application of fundamental concepts with limited originality and a somewhat appropriate research design, reflecting only partial awareness of existing literature. Data interpretation is basic with few methodologies applied, and the conclusions offer minimal contribution to the field, lacking strong support from the findings.\
    Unacceptable (1): The Capstone Project lacks application of fundamental concepts and demonstrates minimal connection to current research, with a problem statement that is unoriginal or duplicative. Data interpretation is flawed, the discussion is weak, and conclusions are unsupported, resulting in little relevance or contribution to the field.\
    ."):
    
    image1_base64 = encode_image_to_base64(image_path1)
   
    

   
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [image1_base64,],
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "No response text returned.")

    except requests.RequestException as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gemma3_vision_insight.py <image_path>")
        sys.exit(1)

    image1_path = sys.argv[1]
    
    insights = query_gemma3_vision(image1_path)
    print("=== Insights Extracted ===")
    print(insights)


 