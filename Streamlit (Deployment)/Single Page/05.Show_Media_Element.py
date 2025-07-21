import streamlit as st
from PIL import Image


# Header
st.header("Learning Show Media Element")
st.write("")
st.write("_________________________________________________________________")

# Image
## If File in folder, use this :
# image_1 = Image.open('Streamlit Logo Primary.png')
# st.image(image_1, caption='Gambar Streamli', width=100, use_column_width=True)

## If File from link, use this :
st.image('https://miro.medium.com/v2/resize:fit:828/format:webp/0*6joPY8VbFO-u41pY.png', caption='Gambar Streamlit')

# Audio
## If File in folder, use this :
# audio_file = open('myaudio.ogg', 'rb')
# audiotest = audio.read()
# st.audio(audiotest,format='audio/oga')

## If File from link, use this :
st.write("This Audio : ")
st.audio("https://example.com/myaudio.mp3",format="audio/mp3")
