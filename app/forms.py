import streamlit as st
from fastai.vision import load_learner, open_image

# load serialized files
import pickle
from shapash.utils.load_smartpredictor import load_smartpredictor

# data manipulation tools
import numpy as np
import pandas as pd

# for shapash plots
from plotly.graph_objs import *
import plotly.graph_objects as go

# ploting the shapash plots require this data
cancer = pd.read_csv('../data/cancer.csv').drop(columns=['outcome'])
kidney = pd.read_csv('../data/kidney.csv').drop(columns=['outcome'])

# pickle-files (shapash models)
model_kidney   = load_smartpredictor('../serialized_files/shapash/kidney/kidney.pkl')
model_cancer   = load_smartpredictor('../serialized_files/shapash/cancer/cancer.pkl')

# pickel-files
model_heart    = pickle.load(open('../serialized_files/pickle/heart.pkl','rb'))
model_liver    = pickle.load(open('../serialized_files/pickle/liver.pkl','rb'))
model_diabetes = pickle.load(open('../serialized_files/pickle/diabetes.pkl','rb'))


# image pickel-files
learn_inf_mal = load_learner('../serialized_files/image/', file='malaria.pkl')
learn_inf_pne = load_learner('../serialized_files/image/', file='pneumonia.pkl')

def heart_form():

    st.title(" Test Your Heart ")

    age      = st.number_input("age", min_value=0, value=0, step=1)
    cp       = st.number_input("cp", min_value=0, value=0, step=1)
    trestbps = st.number_input("trestbps", min_value=0, value=0, step=1)
    chol     = st.number_input("chol", min_value=0, value=0, step=1)
    fbs      = st.number_input("fbs", min_value=0, value=0, step=1)
    restecg  = st.number_input("restecg", min_value=0, value=0, step=1)
    thalach  = st.number_input("thalach", min_value=0, value=0, step=1)
    exang    = st.number_input("exang", min_value=0, value=0, step=1)
    oldpeak  = st.number_input("oldpeak", min_value=0, value=0, step=1)
    slope    = st.number_input("slope", min_value=0, value=0, step=1)
    ca       = st.number_input("ca", min_value=0, value=0, step=1)
    thal     = st.number_input("thal", min_value=0, value=0, step=1)
    
    if st.button('classify'):
        prediction = model_heart.predict([[age,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])[0]
        if prediction == 1:
            st.write("Coronary Artery Disease")
        else:
            st.write("Healthy Heart")


def diabetes_form():

    st.title("Are you diabetic?")

    pregnancies   = st.number_input("pregnancies", min_value=0, value=0, step=1)
    glucose       = st.number_input("glucose-level", min_value=0, value=0, step=1)
    bloodPressure = st.number_input("bloodPressure", min_value=0, value=0, step=1)
    skinThickness = st.number_input("SkinThickness", min_value=0, value=0, step=1)
    insulin       = st.number_input("insulin-level", min_value=0, value=0, step=1)
    BMI           = st.number_input("BMI")
    dpf           = st.number_input("diabetesPedigreeFunction")
    age           = st.number_input("age", min_value=0, value=0, step=1)

    if st.button('classify'):
        prediction = model_diabetes.predict([[pregnancies, glucose, bloodPressure, skinThickness, insulin, BMI, dpf, age]])[0]
        if prediction == 0:
            st.write("NonDiabetic")
        else:
            st.write("Signs of Diabetes")


def liver_form():

    st.title("Is your liver alright?")

    age = st.number_input("age", min_value=0, value=0, step=1)
    tb  = st.number_input("Total_Bilirubin")
    ap  = st.number_input("Alkaline_Phosphotase", min_value=0, value=0, step=1)
    al  = st.number_input("Alamine_Aminotransferase", min_value=0, value=0, step=1) 
    asp = st.number_input("Aspartate_Aminotransferase", min_value=0, value=0, step=1)
    tp  = st.number_input("Total_Protiens")
    abm = st.number_input("Albumin")
    alb = st.number_input("Albumin_and_Globulin_Ratio")

    if st.button('classify'):
        prediction = model_liver.predict([[ age, tb, ap, al, asp, tp, abm, alb]])[0]
        if prediction == 1:
            st.write("Signs of Liver Damage")
        else:
            st.write("NoInfections")
    
   
def cancer_form():
    
    st.title("What is that lump on your chest?")

    radius_mean        = st.number_input("radius_mean")
    perimeter_mean     = st.number_input("perimeter_mean")
    area_mean          = st.number_input("area_mean")
    compactness_mean   = st.number_input("compactness_mean")
    concavity_mean     = st.number_input("concavity_mean")
    concavepoints_mean = st.number_input("concavepoints_mean")
    radius_se          = st.number_input("radius_se")
    perimeter_se       = st.number_input("perimeter_se")
    area_se            = st.number_input("area_se")
    radius_worst       = st.number_input("radius_worst")
    perimeter_worst    = st.number_input("perimeter_worst")
    area_worst         = st.number_input("area_worst")
    compactness_worst  = st.number_input("compactness_worst")
    concavity_worst    = st.number_input("concavity_worst")
    concavepoint_worst = st.number_input("concavepoints_worst")

    if st.button('classify'):

        data = [radius_mean, perimeter_mean, area_mean, compactness_mean, concavity_mean, concavepoints_mean, radius_se, 
                perimeter_se, area_se, radius_worst, perimeter_worst, area_worst, compactness_worst, concavity_worst, concavepoint_worst]
        
        new_cancer = pd.DataFrame(columns = cancer.columns)
        new_cancer.loc[len(cancer)] = data

        new_cancer = new_cancer.astype(cancer.dtypes.to_dict())
        new_cancer.reset_index(inplace = True, drop = True)
        
        model_cancer.add_input(x=new_cancer)

        detailed_contributions = model_cancer.detail_contributions()
        
        if all(detailed_contributions['ypred'] == 1):
            outcome = 'Malignant Tumor'
        else:
            outcome = 'Benign Tumor'
        
        st.write(outcome)


        df = detailed_contributions.drop(['ypred','proba'], axis=1).T.reset_index()
        df.columns= ['features','contribution']
        df = df.sort_values(by='contribution', ascending=True)

        df["color"] = np.where(df["contribution"]<0, '#f4c000', '#4a628a')

        fig = go.Figure(go.Bar(x=df['contribution'], 
                            y=df['features'],
                            orientation='h', 
                            marker_color=df['color']) 
                    )
        fig.update_layout(template='plotly_white', title=outcome, title_x=0.5, xaxis_title="Contribution")

        st.plotly_chart(fig)


def kidney_form():
    
    st.title("Are you drinking enough water?")

    age = st.number_input("age", min_value=0, value=0, step=1)
    bp  = st.number_input("bloodPressure")
    sg  = st.number_input("specificGravity")
    al  = st.number_input("albumin")
    su  = st.number_input("sugar")
    pcc = st.number_input("pusCellClumps", min_value=0, max_value=1, value=0, step=1)
    ba  = st.number_input("bacteria", min_value=0, max_value=1, value=0, step=1)
    bgr = st.number_input("bloodGlucoseRandom")
    bu  = st.number_input("bloodUrea")
    sc  = st.number_input("serumCreatinine")
    sod = st.number_input("sodium")
    pot = st.number_input("potassium")
    glo = st.number_input("hemoglobin")
    pcv = st.number_input("packed cell volume")
    wc  = st.number_input("white blood cell count")
    rc  = st.number_input("red blood cell count")
    dm  = st.number_input("diabetesMellitus", min_value=0, max_value=1, value=0, step=1)
    cad = st.number_input("coronaryArtery", min_value=0, max_value=1, value=0, step=1)
    pe  = st.number_input("pedalEdema", min_value=0, max_value=1, value=0, step=1)

    if st.button('classify'):
        data = [ age, bp, sg, al, su, pcc, ba, bgr, bu, sc, sod, pot, glo, pcv, wc, rc, dm, cad, pe]
        new_kidney = pd.DataFrame(columns = kidney.columns)
        new_kidney.loc[len(kidney)] = data

        new_kidney = new_kidney.astype(kidney.dtypes.to_dict())
        new_kidney.reset_index(inplace = True, drop = True)
        model_kidney.add_input(x=new_kidney)

        detailed_contributions = model_kidney.detail_contributions()
        if all(detailed_contributions['ypred'] == 1):
            outcome = 'CKD'
        else:
            outcome = '~CKD'
        
        st.write(outcome)
        
        df = detailed_contributions.drop(['ypred','proba'], axis=1).T.reset_index()
        df.columns= ['features','contribution']
        df = df.sort_values(by='contribution', ascending=True)

        df["color"] = np.where(df["contribution"]<0, '#f4c000', '#4a628a')

        fig = go.Figure(go.Bar(x=df['contribution'], 
                            y=df['features'],
                            orientation='h', 
                            marker_color=df['color']) 
                    )
        fig.update_layout(template='plotly_white', title=outcome, title_x=0.5, xaxis_title="Contribution")

        st.plotly_chart(fig)

def get_predictions():
    add_selectbox = st.sidebar.selectbox("Make Predictions",
        ("Breast Cancer", "Heart Disease", "Kidney Problem", "Diabetes", "Liver Problem", "Malaria", "Pneumonia"))

    if add_selectbox == "Heart Disease":
        heart_form()

    if add_selectbox == "Diabetes":
        diabetes_form()

    if add_selectbox == "Kidney Problem":
        kidney_form()

    if add_selectbox == "Liver Problem":
        liver_form()

    if add_selectbox == "Breast Cancer":
        cancer_form()
    
    if add_selectbox == "Pneumonia":
        st.title("Upload the Image")
        img = st.file_uploader(label="Image")

        if img:
            label = learn_inf_pne.predict(open_image(img))
            for val in label:
                st.write(val)
                break
    
    if add_selectbox == "Malaria":
        st.title("Upload the Image")
        img = st.file_uploader(label="Image")

        if img:
            label = learn_inf_mal.predict(open_image(img))
            for val in label:
                st.write(val)
                break