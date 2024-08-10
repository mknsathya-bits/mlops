import streamlit as st

st.title("Iris flower species prediction")

sl = st.slider("sepel length",min_value=4.0,max_value=8.0,value=5.0,step=0.1)
pl = st.slider("Petel length",min_value=4.0,max_value=8.0,value=5.0,step=0.1)
sw = st.slider("sepel Width",min_value=4.0,max_value=8.0,value=5.0,step=0.1)
pw = st.slider("Petel Width",min_value=4.0,max_value=8.0,value=5.0,step=0.1)

if st.button('Predict'):
    input_data= [(sl,pl,sw,pw)]
    prediction = "versicolor"

    st.write("predicted is",prediction)

