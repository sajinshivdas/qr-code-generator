#----------------------------------------------------------------------------------------------------------------------------
# Imports
import streamlit as st
from PIL import Image
from generate_function import *
import numpy as np
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Title and Logo
title_container = st.beta_container()
col1, col2 = st.beta_columns([1, 5])
image = Image.open('assets/logo.jpg')
with title_container:
    with col1:
       st.image(image)
    with col2:
        st.title('QR Code Generator')
        st.markdown("""
Turn your personal links into QR Codes.
""")
st.title('')
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# User Input
size = 9
clear_on_submit = st.checkbox('Clear on submit')

with st.form(key='my_form', clear_on_submit=clear_on_submit):
    content = st.text_input('Enter Link or Text.')
    logo_file = st.file_uploader("If you want to add a logo to the QR Code, Upload a Logo. (optional)", type=['png','jpeg','jpg'])
    st.text('Note : Prefer to upload a square image')
    submit_button = st.form_submit_button(label='Generate')
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Body
if content:
    st.markdown("<h3 style='text-align: center; color: black;'>Here is your QR Code</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.beta_columns([4,10,4])
    col1.empty()
    if not logo_file:
        qr_image = generate_qr(content, size)
        col2.image(qr_image, caption=f'QR Code Content : {content}', use_column_width=True)
        array = np.asarray(qr_image)
        result = Image.fromarray(array)
        link = image_download(result)

    elif logo_file:
        open("./assets/logo.png", "wb").write(logo_file.getbuffer())
        qr_image = generate_qr(content, logo=True,  size=size)
        col2.image(qr_image, caption=f'QR Code Content : {content}', use_column_width=True)
        image_file = Image.open(qr_image)
        image_file = image_file.convert('RGBA')
        array = np.asarray(image_file)
        result = Image.fromarray(array)
        link = image_download(result)
        
    st.markdown(f"<h4 style='text-align: center; color: black;'>{link}</h4>", unsafe_allow_html=True)
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Links
st.write('')
st.markdown(f"<p style='text-align: center; color: black;'>To decode the contents of a QR Code, visit this <a href=''>QR Code Decoder.</a></p>.", unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------
# Footer
footer="""<style>
#MainMenu {visibility: hidden;}

a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Made in Streamlit by <a href='https://sajinshivdas.com/cybersecurity/infosec-tools-and-utilities/'>Sajin Shivdas</a>.

</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------


#############################################################################################################################
#############################################################################################################################
