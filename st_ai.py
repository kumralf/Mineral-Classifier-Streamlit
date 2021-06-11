def st_anasayfa():    
    import streamlit as st
    from PIL import Image
    import tensorflow as tf
    import cv2
    import numpy as np
    import os
    from st_info import info
    
    st.markdown('<style>body{background-color: #a9a9a9 ; }</style>', unsafe_allow_html=True)
    
    st.markdown("""<style>
                .big-font 
                {
                font-size:60px !important;color: #000000;
                font-family: "stencil", cursive;
                }
                </style>""",
                unsafe_allow_html=True)
    
    st.markdown('<h1 class="big-font">Mineral Classifier</h1>', unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: left; color: #000000;'>Upload a mineral image to find out which mineral it is</h3>", unsafe_allow_html=True)
    st.text('')
    st.text('')
    
    st.sidebar.header("Nesneye Yönelik Programlama")
    st.sidebar.title("Mineral Classifier")
    
    st.sidebar.write("You can upload an image of a mineral. Artificial intelligence will tell which mineral it is"
                     " and what it's features are.")

    
    st.sidebar.info("Furkan Kumral"
                    "\n" "170207034")
         
    st.markdown("""<style>div.stButton > button:first-child {background-color: rgb(255,	255, 255);}</style>""", unsafe_allow_html=True)

    
    import tensorflow as tf
    gpus = tf.config.experimental.list_physical_devices('GPU')
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    
    import keras
    from PIL import Image, ImageOps
    import numpy as np
    import cv2
    
    def header(url, score):
        st.markdown(f'<p style="background-color:#000000;color:#b87333;font-size:48px;border-radius:1%;">{url}  %{score}</p>', unsafe_allow_html=True)
        
   
    from img_classification import classify
    
    uploaded_file = st.file_uploader("PLease upload a mineral image", type="jpg")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        st.image(image, caption='Uploaded Mineral.', use_column_width=True,  channels="BGR")
        st.write("")    

        label, score = classify(image)

        header(label, score)
    
        
    
    if st.button("INFORMATION"):
        uploaded_file = None
        info(label)


    

    
    
    
    
    
    
    
    
    
    
    
