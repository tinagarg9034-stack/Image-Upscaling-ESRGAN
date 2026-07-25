import streamlit as st
import subprocess
import os
import sys
import time


st.set_page_config(
    page_title="AI Image Upscaler",
    page_icon="🖼️",
    layout="wide"
)

st.sidebar.title("🖼️ AI Image Upscaler")

st.sidebar.markdown("""
### Features
- AI-powered image enhancement
- Real-ESRGAN model
- JPG, JPEG & PNG support
- Download enhanced image

### Developer
Tina Garg
B.Tech CSE
""")

st.title("🖼️ AI Image Upscaler using Real-ESRGAN")

st.write(
    "Upload a JPG, JPEG or PNG image and enhance its quality using the Real-ESRGAN AI model."
)

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    os.makedirs("temp", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    input_path = os.path.join("temp", uploaded_file.name)

    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(input_path, caption="Original Image")

    st.write("📄 File Name:", uploaded_file.name)
    st.write("📏 File Size:", round(uploaded_file.size / 1024, 2), "KB")

    if st.button("Enhance Image"):
        with st.spinner("⏳ AI is enhancing your image... Please wait..."):

            command = [
                sys.executable,
                "inference_realesrgan.py",
                "-n", "RealESRGAN_x4plus",
                "-i", "../" + input_path,
                "-o", "../output",
                "--tile", "32",
            "--fp32"
            ]
            start_time =time.time()

            result = subprocess.run(
                command,
                cwd="Real-ESRGAN-master",
                capture_output=True,
                text=True
            )

            end_time = time.time()
            processing_time = end_time - start_time

        output_file = os.path.join(
            "output",
            uploaded_file.name.split(".")[0] + "_out.jpg"
        )

        if os.path.exists(output_file):
            st.success("✅ Upscaling Complete!")
            st.info(f"Processing Time :{processing_time:.2f}seconds")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(input_path, caption="Original Image")

            with col2:
                st.subheader("Enhanced Image")
                st.image(output_file, caption="Upscaled Image")

            with open(output_file, "rb") as file:
                st.download_button(
                "📥 Download Upscaled Image",
                data=file,
                file_name="upscaled_image.jpg",
                mime="image/jpeg"
            )
        else:
            st.error("❌ Upscaling failed.")
            st.code(result.stderr)