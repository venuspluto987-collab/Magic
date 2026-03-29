import streamlit as st
from rembg import remove
from PIL import Image

st.title("🖼️ Background Color Changer")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file)

    st.image(input_image, caption="Original Image", use_column_width=True)

    # Remove background
    output_image = remove(input_image)

    # Select background color
    bg_color = st.color_picker("Pick Background Color", "#ffffff")

    # Convert to RGBA
    output_image = output_image.convert("RGBA")

    # Create background
    bg = Image.new("RGBA", output_image.size, bg_color)

    # Combine foreground + background
    final_image = Image.alpha_composite(bg, output_image)

    st.image(final_image, caption="Final Image", use_column_width=True)

    # Download button
    st.download_button(
        label="Download Image",
        data=final_image.tobytes(),
        file_name="output.png",
        mime="image/png"
    )