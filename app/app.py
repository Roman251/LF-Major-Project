import streamlit as st

# fetch user defined functions
from about import select_box
from forms import get_predictions

nav = st.sidebar.radio("Navigation",["Home", "About", "Make Predictions"])

st.sidebar.markdown(
        """ Developed by Roman Regmi    
            Email : romanregmi@hotmail.com  
            """)

if nav == "Home":
    st.title("Machine Learning in the field of Medicine")

    sentences = ["Machine learning is swiftly infiltrating many areas within the healthcare industry, from diagnosis and prognosis to drug development and epidemiology, with significant potential to transform the medical landscape. Machine learning algorithms can detect patterns associated with diseases and health conditions by studying thousands of healthcare records and other patient data. They can also be trained to detect complications on medical imaging data.",
                 "The increasingly growing number of applications of machine learning in healthcare allows us to glimpse at a future where data, analysis, and innovation work hand-in-hand to help countless patients without them ever realizing it. Soon, it will be quite common to find ML-based applications embedded with real-time patient data available from different healthcare systems in multiple countries, thereby increasing the efficacy of new treatment options which were unavailable before"
                  ]

    for sentence in sentences:
        st.write(sentence)    
    
    st.image("../images/streamlit_images/machine_learning_medicine.jpeg", width=680)

    st.write("Machine learning has virtually endless applications in the healthcare industry. Today, machine learning is helping to streamline administrative processes in hospitals, map and treat infectious diseases and personalize medical treatments.")

if nav == "About":
    select_box()

if nav == "Make Predictions":
    get_predictions()



    

