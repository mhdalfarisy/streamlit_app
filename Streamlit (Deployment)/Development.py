import streamlit as st
import pandas as pd
import os

# Function to translate sidebar options into English
def Var_language_eng(option):
    if option == "Home":
        return "**Home**"
    elif option == "Explore Data":
        return "**Explore Data**"
    
# Function to translate sidebar options into Indonesian
def Var_language_ina(option):
    if option == "Beranda":
        return "**Beranda**"
    elif option == "Explorasi Data":
        return "**Explorasi Data**"   
       
# Function to get translated sidebar option based on language selection
def Var_language_option(option, language):
    if language == "ENG":
        return Var_language_eng(option)
    elif language == "INA":
        return Var_language_ina(option)

def main_menu():
    # st.set_option('deprecation.showfileUploaderEncoding', False)
    
    # Sidebar options for English and Indonesian languages
    Var_language_eng_side_bar = ["Home", "Explore Data"]
    Var_language_ina_side_bar = ["Beranda", "Explorasi Data"]
    
    # Language selection
    Var_language = st.sidebar.radio("Language", ["ENG", "INA"])
    
    # Select sidebar options based on the chosen language
    if Var_language == "ENG":
        Var_language_side_bar_home = st.sidebar.selectbox("**MENU**", Var_language_eng_side_bar, index=0)
    elif Var_language == "INA":
        Var_language_side_bar_home = st.sidebar.selectbox("**MENU**", Var_language_ina_side_bar, index=0)
    
    # Display header based on the selected option
    if Var_language == "ENG":
        st.title("**Web Streamlit - Data Analytic & Data Visualization**")
    else:
        st.title("**Web Streamlit - Data Analyst & Data Visualisasi**")    
    st.markdown("___")
    st.subheader(Var_language_option(Var_language_side_bar_home, Var_language))  
    st.markdown("_")
    
    # Display Title Menu with out selected option
    if Var_language == "ENG" and Var_language_side_bar_home == "Home":
        st.text("Hallo ! 👋")    
    
    ## Choice Type File
    elif Var_language == "ENG" and Var_language_side_bar_home == "Explore Data":
        handle_file_upload("ENG")
    
    elif Var_language == "INA" and Var_language_side_bar_home == "Beranda":
        st.text("Hallo ! 👋")
          
    elif Var_language == "INA" and Var_language_side_bar_home == "Explorasi Data":
        handle_file_upload("INA")

def handle_file_upload(language):
    if language == "ENG":
        var_explore_data = st.radio("Choice type file : ",['CSV','Excel'])
    else:
        var_explore_data = st.radio("Pilih tipe file : ",['CSV','Excel'])

    if var_explore_data == 'CSV':
        if language == "ENG":
            uploaded_file = st.file_uploader(label="Upload your CSV file", type=['csv'])
        else:
            uploaded_file = st.file_uploader(label="Upload file CSV Anda", type=['csv'])
        
        if uploaded_file is not None:
            try:
                # Detect the encoding of the uploaded file
                df = pd.read_csv(uploaded_file)
                st.dataframe(df)  # Display DataFrame using st.dataframe
                var_question_Visualisation = st.text_input("Do you want to create a visualization [Yes/No]:" if language == "ENG" else "Apakah Anda ingin membuat visualisasi [Ya/Tidak]:")
                if var_question_Visualisation == "Yes" or var_question_Visualisation == "Ya" or var_question_Visualisation == "YES" or var_question_Visualisation == "YA" or var_question_Visualisation == "yes" or var_question_Visualisation == 'ya' :
                    st.write("Visualisation" if language == "ENG" else "Visualisasi")
                    # var_name_column = df.columns.tolist()
                    # st.write(f"Columns available: {', '.join(var_name_column)}")
                    df.columns
                    
                    var_choice_colum_x = st.text_input("X :" if language == "ENG" else "X :")
                    var_choice_colum_y = st.text_input("Y :" if language == "ENG" else "Y :")  

                    if var_choice_colum_x and var_choice_colum_y:
                        st.write(f"Variable X: **{var_choice_colum_x}**" if language == "ENG" else f"Variabel X: **{var_choice_colum_x}**")
                        st.write(f"Variable Y: **{var_choice_colum_y}**" if language == "ENG" else f"Variabel Y: **{var_choice_colum_y}**")
                        st.bar_chart(df[[var_choice_colum_x, var_choice_colum_y]].set_index(var_choice_colum_x))

                elif var_question_Visualisation == "No" or var_question_Visualisation == "no":
                    st.write("Thanks, have a good day!" if language == "ENG" else "Terima kasih, semoga harimu menyenangkan!")

                elif var_question_Visualisation == "":
                    st.write("You haven't given an answer yet..." if language == "ENG" else "Anda belum memberikan jawaban... ")

                else:
                    # st.write("Thanks, have a good day!" if language == "ENG" else "Terima kasih, semoga harimu menyenangkan!")
                    st.write("Your choice is wrong, input true or false" if language == "ENG" else "Jawaban anda salah, input jawaban yang benar")
                
            except Exception as e:
                st.error(f"Error reading the CSV file: {e}")
                
    elif var_explore_data == 'Excel':
        if language == "ENG":
            uploaded_file = st.file_uploader("Upload your Excel file", type=['xlsx'])
        else:
            uploaded_file = st.file_uploader("Upload file Excel Anda", type=['xlsx'])
        
        if uploaded_file is not None:
            try:
                df = pd.read_excel(uploaded_file)
                st.dataframe(df)  # Display DataFrame using st.dataframe
                # You can add additional logic for visualization here
                var_question_Visualisation = st.text_input("Do you want to create a visualization [Yes/No]:" if language == "ENG" else "Apakah anda ingin membuat visualisasi [Ya/Tidak]")
                if var_question_Visualisation == "Yes" or var_question_Visualisation == "Ya" or var_question_Visualisation == "YES" or var_question_Visualisation == "YA" or var_question_Visualisation == "yes" or var_question_Visualisation == 'ya' :
                    st.write("Visualisation" if language == "ENG" else "Visualisasi")
                    # var_name_column = df.columns.tolist()
                    # st.write(f"Columns available: {', '.join(var_name_column)}")
                    df.columns
                    
                    var_choice_colum_x = st.text_input("X :" if language == "ENG" else "X :")
                    var_choice_colum_y = st.text_input("Y :" if language == "ENG" else "Y :")  

                    if var_choice_colum_x and var_choice_colum_y:
                        st.write(f"Variable X: **{var_choice_colum_x}**" if language == "ENG" else f"Variabel X: **{var_choice_colum_x}**")
                        st.write(f"Variable Y: **{var_choice_colum_y}**" if language == "ENG" else f"Variabel Y: **{var_choice_colum_y}**")
                        st.bar_chart(df[[var_choice_colum_x, var_choice_colum_y]].set_index(var_choice_colum_x))

                elif var_question_Visualisation == "No" or var_question_Visualisation == "no":
                    st.write("Thanks, have a good day!" if language == "ENG" else "Terima kasih, semoga harimu menyenangkan!")

                elif var_question_Visualisation == "":
                    st.write("You haven't given an answer yet..." if language == "ENG" else "Anda belum memberikan jawaban... ")

                else:
                    # st.write("Thanks, have a good day!" if language == "ENG" else "Terima kasih, semoga harimu menyenangkan!")
                    st.write("Your choice is wrong, input true or false" if language == "ENG" else "Jawaban anda salah, input jawaban yang benar")
                
            except Exception as e:
                st.error(f"Error reading the Excel file: {e}")

if __name__ == "__main__":
    main_menu()

    

# streamlit run Development.py --server.enableXsrfProtection false
