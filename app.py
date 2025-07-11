import streamlit as st
from PIL import Image
from colorthief import ColorThief
from utils.color_extraction import extract_palette
from utils.pdf_export import create_pdf
from utils.style_detection import detect_style
import os

st.set_page_config(page_title="Moodboard & Color Palette Generator", layout="centered")
st.title("Moodboard & Color Palette Generator 🎨")

uploaded_files = st.file_uploader("Upload inspiration images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

if uploaded_files:
    st.write("Preview of Uploaded Images:")
    images = []
    all_palettes = []

    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        images.append(image)
        st.image(image, width=150)

        # Extract color palette
        temp_path = f"temp_{uploaded_file.name}"
        image.save(temp_path)
        palette = extract_palette(temp_path, color_count=6)
        all_palettes.append(palette)
        os.remove(temp_path)

    st.write("## Extracted Color Palettes:")
    for palette in all_palettes:
        for color in palette:
            st.markdown(f"<div style='background-color: rgb{color}; height: 50px;'></div>", unsafe_allow_html=True)

    # Simple horizontal moodboard
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    moodboard = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        moodboard.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    st.write("## Generated Moodboard:")
    st.image(moodboard)

    # Save and download moodboard
    moodboard_path = "moodboard.jpg"
    moodboard.save(moodboard_path)

    with open(moodboard_path, "rb") as file:
        st.download_button(label="Download Moodboard", data=file, file_name="moodboard.jpg", mime="image/jpeg")

    # Export to PDF
    if st.button("Export Moodboard & Palette as PDF"):
        pdf_path = "moodboard.pdf"
        create_pdf(moodboard_path, all_palettes, filename=pdf_path)
        with open(pdf_path, "rb") as file:
            st.download_button(label="Download PDF", data=file, file_name="moodboard.pdf", mime="application/pdf")

    # Detect style
    if st.button("Detect Style"):
        style = detect_style(uploaded_files)
        st.write(f"Predicted Style: {style}")
