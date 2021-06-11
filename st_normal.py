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
    
    st.markdown('<h1 class="big-font">Select a Mineral</h1>', unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: left; color: #000000;'>Select the mineral that you want to get information.</h3>", unsafe_allow_html=True)
    
    st.sidebar.header("Nesneye Yönelik Programlama")
    st.sidebar.title("Select a Mineral")
    
    st.sidebar.write("You can choose the mineral you want to get information from below.")
    
    minerals = ['Amethyst', 'Boron', 'Galena', 'Halite', 'Chalcopyrite',
                'Chromite', 'Quartz', 'Malachite', 'Obsidian', 'Pyrite'] 
    
    


    select = {0:"select", 1:"Amethyst", 2:'Boron', 3:'Galena', 4:'Halite', 5:'Chalcopyrite',
                6:'Chromite', 7:'Quartz', 8:'Malachite', 9:'Obsidian', 10:'Pyrite'}
    

    def format_func(option):
        return select[option]


    option = st.selectbox("", options=list(select.keys()), format_func=format_func)
    
    if option == 1:
        img = Image.open("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/ametist/5.jpg")
        st.image(img, channels="BGR")
        info(select[1])
        
    elif option == 2:
        img = Image.open("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/bor/8.jpg")
        st.image(img, channels="BGR")
        info(select[2])
        
    elif option == 3:
        img = Image.open("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/galen/13.jpg")
        st.image(img, channels="BGR")
        info(select[3])
        
    elif option == 4:
        img = Image.open("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/halit/18.jpg")
        st.image(img, channels="BGR")
        info(select[4])
        
    elif option == 5:
        img = Image.open("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/kalkopirit/17.jpg")
        st.image(img, channels="BGR")
        info(select[5])
        
    elif option == 6:
        img = Image.open("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/kromit/18.jpg")
        st.image(img, channels="BGR")
        info(select[6])
        
    elif option == 7:
        img = Image.open("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/kuvars/15.jpg")
        st.image(img, channels="BGR")
        info(select[7])
        
    elif option == 8:
        img = Image.open("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/malakit/21.jpg")
        st.image(img, channels="BGR")
        info(select[8])
        
    elif option == 9:
        img = Image.open("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/obsidyen/24.jpg")
        st.image(img, channels="BGR")
        info(select[9])
        
    elif option == 10:
        img = Image.open("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/pirit/26.jpg")
        st.image(img, channels="BGR")
        info(select[10])

    
    st.sidebar.info("Furkan Kumral"
                    "\n" "170207034")
    

 

