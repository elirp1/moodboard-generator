import streamlit as st
from PIL import Image
from colorthief import ColorThief
import os

st.title("Moodboard & Color Palette Generator")

uploaded_files = st.file_uploader("Upload inspiration images", accept_multiple_files=True)

if uploaded_files:
    st.write("Preview of Uploaded Images:")
    images = []
    palette = []
    
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        images.append(image)
        st.image(image, width=150)

        # Save temporarily
        temp_path = f"temp_{uploaded_file.name}"
        image.save(temp_path)
        color_thief = ColorThief(temp_path)
        dominant_color = color_thief.get_color(quality=1)
        palette.append(dominant_color)
        os.remove(temp_path)

    # Display color palette
    st.write("Extracted Color Palette:")
    for color in palette:
        st.markdown(f"<div style='background-color: rgb{color}; height: 50px;'></div>", unsafe_allow_html=True)

    # Simple horizontal collage
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    moodboard = Image.new('RGB', (total_width, max_height))
    
    x_offset = 0
    for im in images:
        moodboard.paste(im, (x_offset,0))
        x_offset += im.size[0]
    
    st.write("Generated Moodboard:")
    st.image(moodboard)

    # Download option
    moodboard.save("moodboard.jpg")
    with open("moodboard.jpg", "rb") as file:
        btn = st.download_button(label="Download Moodboard", data=file, file_name="moodboard.jpg", mime="image/jpeg")
