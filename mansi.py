import streamlit as st
st.set_page_config(page_title='MAnsi',page_icon='random')
mymenu=st.sidebar.selectbox('MyMenu',('home','form','cart'))
st.title('Mansi Yadav')
st.image('https://www.alstom.com/sites/alstom.com/files/styles/560w/public/2023/08/28/Picture1.jpg?itok=KI3I10VV')
st.header('By myself')
st.text('Believe in yourself')
if(mymenu=='home'):
    st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
    st.video('https://youtu.be/eKPZNmI62c4?si=xcnq-38KToHjtxZ2')
elif(mymenu=='form'):
    with st.form('My Form'):
        name=st.text_input('Name:')
        city=st.text_input('City:')
        dob=st.date_input('DOB:')
        marks=st.slider('marks')
        k=st.form_submit_button('Submit')
        if k:
            st.write(name,city,marks,dob)
elif(mymenu=='cart'):
    st.header('Downloads')
    st.download_button('Download Now','hello this is the downloade data','mansi.txt')
    
    
