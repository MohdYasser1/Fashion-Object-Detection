import streamlit as st
from PIL import Image, ImageDraw
from ultralytics import YOLO
import pandas as pd

# Load the pre-trained model
model = YOLO("fashion_yolo.pt")



def classify_image(image):
    results = model.predict(image)
    return results

def draw_bounding_boxes(image, results):
    draw = ImageDraw.Draw(image)
    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        cls = int(box.cls[0].item())
        label = results[0].names[cls]
        confidence = box.conf[0].item()
        draw.text((x1, y1), f"{label} ({confidence:.2f})", fill="red")
        draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
    return image

def count_objects(results):
    counts = {}
    for box in results[0].boxes:
        cls = int(box.cls[0].item())
        label = results[0].names[cls]
        if label in counts:
            counts[label] += 1
        else:
            counts[label] = 1
    return counts

# Streamlit app
st.title("Image Component Analysis")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    image_view = st.empty()
    image_view.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Analyse Image"):
        with st.spinner("Analysing..."):
            results = classify_image(image)
            image_with_boxes = draw_bounding_boxes(image.copy(), results)
            object_count = count_objects(results)
        image_view.image(image_with_boxes, caption="Image with Bounding Boxes", use_column_width=True)
        st.write("Detected Components:")
        object_count_df = pd.DataFrame(list(object_count.items()), columns=["Component", "Count"])
        st.table(object_count_df)
