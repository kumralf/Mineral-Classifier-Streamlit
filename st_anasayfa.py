import st_ai
import st_normal
import streamlit as st


PAGES = {
    "Upload a mineral image to find out which mineral it is": st_ai,
    "Select a Mineral to get information": st_normal
}
st.sidebar.title('Classify or Select')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.st_anasayfa()

st.sidebar.text("")
st.sidebar.text("")


import pandas as pd

@st.cache(allow_output_mutation=True)
def get_data():
    return []

user_id = st.sidebar.text_input("User-ID")
mineral =  st.sidebar.text_input("Mineral Suggestion")
    

if st.sidebar.button("Submit"):
    get_data().append({"User-ID": user_id, "Mineral Suggestion": mineral})

st.sidebar.write(pd.DataFrame(get_data()))
		