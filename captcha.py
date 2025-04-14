import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import string
import io

def generate_captcha_text(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_captcha_image(captcha_text):
    image = Image.new('RGB', (150, 50), color = (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Optional: custom font
    # font = ImageFont.truetype("arial.ttf", 36)

    draw.text((10, 5), captcha_text, fill=(0, 0, 0))  # , font=font)
    return image

st.title("🛡️ Captcha Demo")

# Generate captcha
if 'captcha' not in st.session_state:
    st.session_state.captcha = generate_captcha_text()

captcha_image = generate_captcha_image(st.session_state.captcha)

# Display captcha image
buf = io.BytesIO()
captcha_image.save(buf, format="PNG")
st.image(buf.getvalue())

# User input
user_input = st.text_input("Enter the captcha above")

if st.button("Verify"):
    if user_input.upper() == st.session_state.captcha:
        st.success("✅ Captcha verified!")
        st.session_state.captcha = generate_captcha_text()  # Refresh captcha
    else:
        st.error("❌ Incorrect captcha. Try again.")
