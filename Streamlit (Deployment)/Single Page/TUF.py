# import streamlit as st
# from pathlib import Path


# st.title("Demo")
# # st.image(res, width = 800)

# st.markdown("**Please fill the below form :**")
# with st.form(key="Form :", clear_on_submit = True):
#     Name = st.text_input("Name : ")
#     Email = st.text_input("Email ID : ")
#     File = st.file_uploader(label = "Upload file", type=["pdf","docx"])
#     Submit = st.form_submit_button(label='Submit')
    

# st.subheader("Details : ")
# st.metric(label = "Name :", value = Name)
# st.metric(label = "Email ID :", value = Email)

# if Submit :
#     st.markdown("**The file is sucessfully Uploaded.**")

#     # Save uploaded file to 'F:/tmp' folder.
#     save_folder = 'F:/tmp'
#     save_path = Path(save_folder, File.name)
#     with open(save_path, mode='wb') as w:
#         w.write(File.getvalue())

#     if save_path.exists():
#         st.success(f'File {File.name} is successfully saved!')

# ----
# import os
# import streamlit as st

# # Function to save uploaded file to a specified folder
# def save_uploaded_file(uploaded_file, save_folder):
#     if not os.path.exists(save_folder):
#         os.makedirs(save_folder)
#     with open(os.path.join(save_folder, uploaded_file.name), "wb") as f:
#         f.write(uploaded_file.getbuffer())
#     return os.path.join(save_folder, uploaded_file.name)

# # Streamlit UI
# st.title("File Uploader and Saver")

# # File uploader component
# uploaded_file = st.file_uploader("Upload File Here:", type=["csv", "txt"])

# # Specify the folder where the uploaded files will be saved
# save_folder = 'uploads'

# # Check if a file has been uploaded
# if uploaded_file is not None:
#     # Display some information about the uploaded file
#     file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
#     st.write(file_details)

#     # Save the uploaded file to the specified folder
#     saved_path = save_uploaded_file(uploaded_file, save_folder)
#     st.success(f"File saved successfully at: {saved_path}")

# ----
import os
import streamlit as st

# Function to save uploaded file to a specified folder
def save_uploaded_file(uploaded_file, save_folder):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    with open(os.path.join(save_folder, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return os.path.join(save_folder, uploaded_file.name)

# Streamlit UI
st.title("File Uploader and Saver")

# File uploader component
uploaded_file = st.file_uploader("Upload File Here:", type=["csv", "txt"])

# Specify the folder where the uploaded files will be saved
save_folder = r'D:\Training SSIS + Python + Streamlit\Streamlit (Deployment)\Single Page'

# Check if a file has been uploaded
if uploaded_file is not None:
    # Display some information about the uploaded file
    file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    st.write(file_details)

    # Save the uploaded file to the specified folder
    saved_path = save_uploaded_file(uploaded_file, save_folder)
    st.success(f"File saved successfully at: {saved_path}")
