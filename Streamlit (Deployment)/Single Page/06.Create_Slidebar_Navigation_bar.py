import streamlit as st


st.header("Learn Streamlit for Create Navigation")

## Sidebar Radio
st.sidebar.subheader("Example Sidebar Radio Text")
st.sidebar.radio("Navigation", ['Home','About Us','Contact Us'])

## Sidebar Selectionbox
st.sidebar.subheader("Example Sidebar Select Box")
st.sidebar.selectbox("Navigation",['Home','About Us','Contact US'])

## Sidebar Multiselect
st.sidebar.subheader("Example Sidebar Multiselect")
st.sidebar.selectbox("Navigation",['Home','About Us','Contact Us'])

## Sidebar Input Number
st.sidebar.subheader("Example Sidebar Input Number")
st.sidebar.number_input("Choice Number : ",1,3)

## Sidebar Radio Number
st.sidebar.subheader("Example Sidebar Radio Number")
st.sidebar.radio(label="Navigation",options=[10,20,30])

## Sidebar File Upload
st.sidebar.subheader("Example Sidebar File Upload")
st.sidebar.file_uploader("Upload File :",type=['csv','txt'])

# ---- Train with Conditional IF
st.sidebar.subheader("Example Sidebar Radio Text")
Choice_ = st.sidebar.radio("Navigation", ['Image','Audio','Video'])

if Choice_ == "Image":
    st.header("Image :")
    st.image('https://miro.medium.com/v2/resize:fit:828/format:webp/0*6joPY8VbFO-u41pY.png', caption='Gambar Streamlit')

if Choice_ == "Audio":
    st.header("Audio :")
    st.audio("https://example.com/myaudio.mp3",format="audio/mp3")

if Choice_ == "Video":
    st.header("Video :")
    st.video("")    


