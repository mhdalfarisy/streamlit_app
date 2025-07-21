# ---- VISUALISASI STREAMLIT USE MATPLOTLIB
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", initial_sidebar_state="auto")

var_header = st.header("**Explore Data and Visualization**")
var_markdown_1 = st.markdown("___")


## ---- TAB FITUR PILIHAN : DATA / SETTING
tabs = st.tabs(["Data","Setting"])

## ---- FUCTION FITUR SETTING
def setting_data():
    var_header_name = st.text_input('***Header Name :***')
    var_label_x_name = st.text_input('***X Label :***')
    var_label_y_name = st.text_input('***Y Label :***')
    var_width_size = st.number_input('***Width Size :***')
    st.text('You can custom this color with click Pic a Color :')
    var_color = st.color_picker('')
    var_choice_color_picker = var_color
    return var_header_name, var_label_x_name, var_label_y_name, var_width_size, var_choice_color_picker

## ---- FUCTION FITUR DATA
def explore_data_menu():
    ## ---- FITUR SETTING
    with tabs[1]:
        var_header_name, var_label_x_name, var_label_y_name, var_width_size,var_choice_color_picker = setting_data()

    ## ---- FITUR DATA
    with tabs[0]:

        ## ---- FITUR URL
        var_radio_choice = st.selectbox("Choice Upload File: ", ['URL CSV', 'Upload CSV', 'Upload XLSX'], index=None)
        if var_radio_choice == 'URL CSV':
            var_input_url = st.text_input('Input URL : ')
            if var_input_url:
                try:
                    var_input_url_result = pd.read_csv(var_input_url)
                    st.write("Dataset : ")
                    st.dataframe(var_input_url_result)
                    df = var_input_url_result
                except Exception as Information_Input_URL:
                    st.error("Error : Unable to read the URL CSV File")

                var_choice_x = st.selectbox("Choice Variabel X:",df.columns, index=None)
                var_choice_y = st.selectbox("Choice Variabel Y:", df.columns, index=None)

                if var_choice_x is not None and var_choice_y is not None:
                    try:
                        plt.figure(figsize=(20,5))
                        plt.bar(df[var_choice_x],df[var_choice_y],color=var_choice_color_picker, width = var_width_size)
                        plt.title(var_header_name)
                        plt.xlabel(var_label_x_name)
                        plt.ylabel(var_label_y_name)
                        plt.xticks(df[var_choice_x], rotation=0, ha='right') 
                        st.pyplot(plt)
                    except Exception as Information_Upload_Excel:
                        st.error("Error : Unable to Visualisation")              

        ## ---- FITUR CSV
        elif var_radio_choice == 'Upload CSV':
            var_upload_csv = st.file_uploader(label='Upload CSV : ', type=['csv'])
            if var_upload_csv is not None:
                save_path = "D:\Training SSIS + Python + Streamlit\Streamlit (Deployment)"
                os.makedirs(save_path, exist_ok=True)
                file_path = os.path.join(save_path, var_upload_csv.name)
                with open(file_path, "wb") as f:
                    f.write(var_upload_csv.getbuffer())
                try:
                    df = pd.read_csv(file_path)
                    st.write(df)
                    var_radio_choice_notification = st.text("File success upload and save in : {}".format(file_path))
                    var_df_column = df.columns
                except Exception as Information_Upload_CSV:
                    st.error("Error : Unable to read the Upload CSV File")

                var_choice_x = st.selectbox("Choice Variabel X : ", df.columns, index=None)
                var_choice_y = st.selectbox("Choice Variabel Y : ", df.columns, index=None)

                if var_choice_x is not None and var_choice_y is not None:
                    try:
                        plt.figure(figsize=(20, 5))
                        plt.bar(df[var_choice_x], df[var_choice_y], color=var_choice_color_picker,width = var_width_size)
                        plt.title(var_header_name)
                        plt.xlabel(var_label_x_name,fontsize=10)
                        plt.ylabel(var_label_y_name)
                        plt.xticks(df[var_choice_x], rotation=45, ha='right')
                        st.pyplot(plt)
                    except Exception as Information_Upload_Excel:
                        st.error("Error : Unable to Visualization")

        ## ---- FITUR EXCEL
        elif var_radio_choice == 'Upload XLSX':
            var_upload_xlsx = st.file_uploader(label='Upload XLSX:', type=['xlsx'])
            if var_upload_xlsx is not None:
                save_path = "D:\\Training SSIS + Python + Streamlit\\Streamlit (Deployment)"
                os.makedirs(save_path, exist_ok=True)
                file_path = os.path.join(save_path, var_upload_xlsx.name)
                with open(file_path, "wb") as f:
                    f.write(var_upload_xlsx.getbuffer())
                try:
                    df = pd.read_excel(file_path)
                    st.write(df)
                    var_radio_choice_notification = st.text("File success upload and save in : {}".format(file_path))
                    var_df_column = df.columns
                except Exception as Information_Upload_CSV:
                    st.error("Error : Unable to read the Upload CSV File")

                var_choice_x = st.selectbox("Choice Variabel X : ", df.columns, index=None)
                var_choice_y = st.selectbox("Choice Variabel Y : ", df.columns, index=None)

                if var_choice_x is not None and var_choice_y is not None:
                    try:
                        plt.figure(figsize=(20, 5))
                        plt.bar(df[var_choice_x], df[var_choice_y], color=var_choice_color_picker,width = var_width_size)
                        plt.xlabel(var_label_x_name,fontsize=10)
                        plt.ylabel(var_label_y_name)
                        plt.title(var_header_name)
                        plt.xticks(df[var_choice_x], rotation=45, ha='right')
                        st.pyplot(plt)
                    except Exception as Information_Upload_Excel:
                        st.error("Error : Unable to Visualization")


if __name__ == "__main__":
    explore_data_menu()
 
# # https://gist.githubusercontent.com/hbuddana/4f32e8e8b1bcfa39c146ae8dde81b9a0/raw/f9f94e3818d37b3286e744b961432b6a4cf64fbe/Salesdata.csv   -


# streamlit run Data Visualisasi.py --server.enableXsrfProtection false

