import streamlit as st


st.header("Learn Widget in Streamlit with Python")
st.subheader("______________________________________________________________________________")

st.markdown("""
            1. Create Button
            
            2. Create Checkbox
            
            3. Create Radio Button
            
            4. Selectbox
            
            5. Multiselect

            6. Slider & Select-slider

            7. Input Text

            8. Input Number

            9. Text Area

            10. Date Input

            11. Time Input

            12. File Upload

            13. Color Picker

            """,True)

st.subheader("______________________________________________________________________________")

# 1. Cara buat Widget Buttom di Streamlit
st.subheader("Example Buttom")
if(st.button("Buat Buttom")):
    st.text("Welcome To Playlist Streamlit : ")

# 2. Create Checkbox
st.subheader("Example Checkbox")    
if st.checkbox("Learn A : "):
    st.text("A")
if st.checkbox("Learn B : "):
    st.text("B")

# 3. Create Radio Buttom
st.subheader("Example Radio Buttom")
Status = st.radio("Choice Playlist :",('NLP','Streamlit','Flask'))
st.write("You Choise Modul :",Status,"For Learning")

# 4. Create Selection Box
st.subheader("Example Selection Box")
Single_Box = st.selectbox("Choice : ", ['NLP','Streamlit','Flask'])
st.write("You Choise Modul :",Single_Box,"For Learning")

# 5. Create Multiselection Box
st.subheader("Example Multipleselection Box")
Multiple_Box = st.multiselect("Choice : ", ['NLP','Streamlit','Flask'])
st.write("You Choice Modul :", len(Multiple_Box)," Modul For Learning")

# 6. Create Slider
# st.subheader("Example Slider")
# Status = st.radio("Choice Playlist :",('NLP','Streamlit','Flask'))
# st.write("You Choise Modul :",Status,"For Learning")
# Level = st.slider("Choice Level Modul :", 1, 3)
# st.write('You Choice Level : {}'.format(Level),'From {}'.format(Status))
#--
st.subheader("Example Slider")
Level = st.slider("Choice Level Modul : ",1,3)
st.text('You Choice Level : {}'.format(Level))

# 6. Create Slinder
st.subheader("Example Slinder")
Level_Category = st.select_slider('Choice Level Modul',
                    options=['Basic','Intermediate','Advance'])
st.write('You Choice Level : ',Level_Category)

# 7. Create Input Text
st.subheader("Example Input Text")
Input_Text = st.text_input("Please Input Text :","")
st.write(" ",Input_Text)

# 8. Create Input Number
st.subheader("Example Input Number")
Input_Number = st.number_input("Please Input Number :",1,10)
st.write(" ",Input_Number)

# 9. Create Text Area :
st.subheader("Example Text Area")
Input_Text_Area = st.text_area("Please Input Text Area:","")
st.write(" ",Input_Text_Area)

# 10. Create Input Date
st.subheader("Example Input Date")
Input_Date = st.date_input("Please Input Date :")
st.write("Date You Choice : ",Input_Date)

# 11. Create Input Time
st.subheader("Example Input Time")
Input_Time = st.time_input("Please Input Time :")
st.write("Time You Choice : ",Input_Time)

# 12. Create File Uploader
st.subheader("Example File Uploader")
st.file_uploader("Upload File Here :",type=["csv","txt"])

# 13. Create Color Picker
color = st.color_picker('Picker A Color','#F90000')
st.write('The Current Color Is',color)