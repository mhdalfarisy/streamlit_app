#  Text Elemet
#  Markdown, Title, Header, Subheader, Caption, Code Block, Text, LaTex

# # Import Modul
import streamlit as st

## Title
st.title("Belajar Stramlit")

## Header
st.header("Belajar Buat Header")

## Subheader
st.subheader("Belajar Buat Subheader")

## Text
st.text("Belajar Buat Text")

## Markdown
st.markdown("# Markdown 1")
st.markdown("## Markdown 2")
st.markdown("### Markdown 3")
st.markdown("#### Markdown 4")

## Markdown Multibaris
st.markdown(""" 
# Test1

## Test2
            
### Test3            
""",True)

## Code Block
code_1 = '''def Hello():
        print("Hello, Streamlit)'''
st.code(code_1, language='Python')

code_2 = '''Ini Huruf A'''
st.code(code_2,language='Pyhton')
