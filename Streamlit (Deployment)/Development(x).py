# import streamlit as st
# import pandas as pd
# import numpy as np

# st.set_page_config(page_title='CSV FILE READER',layout='wide')

# # Main Title
# variabel_main_header = st.header("Streamlit Development - Read CSV")
# st.write('_______________________________________________________________________________________________')

# # Sub Title
# variabel_sub_header = st.sidebar.subheader("Menu : ")
# st.sidebar.write('_________________________________________')

# # Menu
# var_slidebar_menu = st.sidebar.radio("Choice",['Upload File (Read CSV)',
#                                                'Input URL (Read CSV)',
#                                                'Github User'
#                                                ])

# ### Error -> AxiosError: Request failed with status code 403
# if var_slidebar_menu == "Upload File (Read CSV)":
#     st.subheader("Upload CSV")
#     data_file = st.file_uploader("Upload CSV",type=["CSV"])
#     if data_file is not None:
#         st.write(type(data_file))

# ### DONE 
# if var_slidebar_menu == "Input URL (Read CSV)":
#     st.subheader("Input URL")        
#     url_file = st.text_input("Input URL :","")
#     if url_file is not None:
#         try :
#             df_url_file = pd.read_csv(url_file)
#             st.write("Dataset : ")
#             st.dataframe(df_url_file)
#         except Exception as note :
#             st.error("Error: Unable to read the uploaded CSV file.",icon="🚨")   

# ### DONE
# if var_slidebar_menu == "Github User":
#     df_github = st.link_button("Go To Github","https://github.com/mhdalfarisy")
    


# # https://gist.githubusercontent.com/hbuddana/4f32e8e8b1bcfa39c146ae8dde81b9a0/raw/f9f94e3818d37b3286e744b961432b6a4cf64fbe/Salesdata.csv


# import streamlit as st
# import pandas as pd
# import os
# # streamlit run Development.py --server.enableXsrfProtection false

# # Function to translate sidebar options into English
# def Var_language_eng(option):
#     if option == "Home":
#         return "**Home**"
#     elif option == "Explore Data":
#         return "**Explore Data**"
    
# # Function to translate sidebar options into Indonesian
# def Var_language_ina(option):
#     if option == "Beranda":
#         return "**Beranda**"
#     elif option == "Explorasi Data":
#         return "**Explorasi Data**"   
       
# # Function to get translated sidebar option based on language selection
# def Var_language_option(option, language):
#     if language == "ENG":
#         return Var_language_eng(option)
#     elif language == "INA":
#         return Var_language_ina(option)

    
# def main_menu():
#     st.set_option('deprecation.showfileUploaderEncoding', False)
    
#     # Sidebar options for English and Indonesian languages
#     Var_language_eng_side_bar = ["Home", "Explore Data"]
#     Var_language_ina_side_bar = ["Beranda", "Explorasi Data"]
    
#     # Language selection
#     Var_language = st.sidebar.radio("Language", ["ENG", "INA"])
    
#     # Select sidebar options based on the chosen language
#     if Var_language == "ENG":
#         Var_language_side_bar_home = st.sidebar.selectbox("**MENU**", Var_language_eng_side_bar, index=0)
#     elif Var_language == "INA":
#         Var_language_side_bar_home = st.sidebar.selectbox("**MENU**", Var_language_ina_side_bar, index=0)
    
#     # Display header based on the selected option
#     if Var_language == "ENG":
#         st.title("**Web Streamlit - Data Analytic & Data Visualization**")
#     else:
#         st.title("**Web Streamlit - Data Analyst & Data Visualisasi**")    
#     st.markdown("___")
#     st.subheader(Var_language_option(Var_language_side_bar_home, Var_language))  
#     st.markdown("_")
    
#     # Display Title Menu with out selected option
#     if Var_language == "ENG" and Var_language_side_bar_home == "Home":
#         # st.write("Home in Progress . . .")
#         st.text("Hallo ! 👋")    
    
#     ## Choice Type File
#     elif Var_language == "ENG" and Var_language_side_bar_home == "Explore Data":
#         var_explore_data = st.radio("Choice type file : ",['CSV','Excel',])
        
#         if var_explore_data == 'CSV':
#             uploaded_file = st.file_uploader(label="Upload you file CSV", type=['csv'])
#             if uploaded_file is not None:
#                 save_path = "D:\Training SSIS + Python + Streamlit\Streamlit (Deployment)"
#                 os.makedirs(save_path, exist_ok=True)
#                 file_path = os.path.join(save_path, uploaded_file.name)
#                 with open(file_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#                 st.success("Upload file sucess and save file at : {}".format(file_path))
#                 df = pd.read_csv(file_path)
#                 st.write(df)
#             var_question_Visualisation = st.text_input("Do you want to create a visualization [Yes/No]:")
#             if var_question_Visualisation == "Yes" or var_question_Visualisation == "yes":
#                 st.write("Visualisation")
#                 var_name_column = df.columns
#                 var_name_column
#                 st.write('Choice Columns : ')
#                 var_choice_colum_x = st.text_input("X : ")
#                 var_choice_colum_y = st.text_input("Y : ")  
#                 var_x = var_choice_colum_x
#                 var_y = var_choice_colum_y      
#                 if var_y != " ":
#                     st.write("Variabel Y is **:**",var_y)          
#                 var_result_x_y = st.bar_chart(df,x=var_x,y=var_y)
#                 if var_result_x_y == " ":
#                     st.write("Is Blank")
#                 else:
#                     var_result_x_y
#             elif var_question_Visualisation == "No" or var_question_Visualisation == "no":
#                 st.write("Thanks, have a good day !")     
#             else:
#                 st.write("If you want to next step for visualisation, input **Yes** and if not do step input **No**")    

                
#         elif var_explore_data == 'Excel':
#             uploaded_file = st.file_uploader("Upload you file Excel", type=['xlsx'])
#             if uploaded_file is not None:
#                 save_path = "D:\Training SSIS + Python + Streamlit\Streamlit (Deployment)"
#                 os.makedirs(save_path,exist_ok=True)
#                 file_path = os.path.join(save_path,uploaded_file.name)
#                 with open(file_path,"wb") as f :
#                     f.write(uploaded_file.getbuffer())
#                 st.success("Upload file Sucess and save file at : {}".format(file_path))
#                 df = pd.read_excel(file_path)
#                 st.write    
                        
    
#     elif Var_language == "INA" and Var_language_side_bar_home == "Beranda":
#         # st.write("Beranda masih di proses . . .")
#         st.text("Hallo ! 👋")
          
#     elif Var_language == "INA" and Var_language_side_bar_home == "Explorasi Data":
#         var_explore_data = st.radio("Pilih tipe file : ",['CSV','Excel'])
        
#         if var_explore_data == 'CSV':
#             uploaded_file = st.file_uploader(label="Upload file CSV anda", type=['csv'])
#             if uploaded_file is not None:
#                 save_path = "D:\Training SSIS + Python + Streamlit\Streamlit (Deployment)"
#                 os.makedirs(save_path, exist_ok=True)
#                 file_path = os.path.join(save_path, uploaded_file.name)
#                 with open(file_path, "wb") as f:
#                     f.write(uploaded_file.getbuffer())            
#                 st.sidebar.success("File berhasil diunggah dan disimpan di: {}".format(file_path))
#                 df = pd.read_csv(file_path)
#                 st.write(df)
                
#         elif var_explore_data == 'Excel':
#             uploaded_file = st.file_uploader(label="Upload file Excel Anda", type=['xlsx'])
#             if uploaded_file is not None:
#                 save_path = "D:\Training SSIS + Python + Streamlit\Streamlit (Deployment)"
#                 os.makedirs(save_path,exist_ok=True)
#                 file_path = os.path.join(save_path,uploaded_file.name)
#                 with open(file_path,"wb") as f :
#                     f.write(uploaded_file.getbuffer())
#                 st.sidebar.success("File berhasil diunggah dan disimpan di: {}".format(file_path))
#                 df = pd.read_csv(file_path)
#                 st.write(df)


                
        
# if __name__ == "__main__":
#     main_menu()