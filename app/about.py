import streamlit as st

def select_box():
    add_selectbox = st.sidebar.selectbox("Understand Your Health",
        ("Breast Cancer", "Heart Disease", "Kidney Problem", "Diabetes", "Liver", "Malaria", "Pneumonia"))

    if add_selectbox == "Breast Cancer":
        st.title("What Is Breast Cancer?")
        st.image("../images/streamlit_images/breast_cancer.jpeg", width=350)
        st.write("Breast cancer is a disease in which cells in the breast grow out of control. They can begin in different parts of the breast and can spread outside the breast through blood vessels and lymph vessels.When breast cancer spreads to other parts of the body, it is said to have metastasized.")

        st.title("Kinds of Breast Cancer")
        st.write("Invasive ductal carcinoma: The cancer cells grow outside the ducts into other parts of the breast tissue. Invasive cancer cells can also spread, or metastasize, to other parts of the body.")
        st.write("Invasive lobular carcinoma: Cancer cells spread from the lobules to the breast tissues that are close by. These invasive cancer cells can also spread to other parts of the body.")
        
        st.title("Symptoms")
        st.write("1. A breast lump or thickening that feels different from the surrounding tissue")
        st.write("2. Change in the size, shape or appearance of a breast")
        st.write("3. Changes to the skin over the breast, such as dimpling")

    
    if add_selectbox == "Heart Disease":
        st.title("Heart Disease")
        st.write("The term “heart disease” refers to several types of heart conditions. The most common type of heart disease in the United States is coronary artery disease (CAD), which affects the blood flow to the heart. Decreased blood flow can cause a heart attack.")

        st.title("What are the Symptoms of heart disease?")
        st.write("Heart attack: Chest pain or discomfort, upper back or neck pain, indigestion, heartburn, nausea or vomiting, extreme fatigue, upper body discomfort, dizziness, and shortness of breath.")
        st.write("Arrhythmia: Fluttering feelings in the chest (palpitations).")
        st.write("Heart failure: Shortness of breath, fatigue, or swelling of the feet, ankles, legs, abdomen, or neck veins.")

        st.image('../images/streamlit_images/heart_condition.jpeg')

        st.title("What are the risk factors for heart disease?")
        st.write("High blood pressure, high blood cholesterol, and smoking are key risk factors for heart disease. About half of Americans (47%) have at least one of these three risk factors.2 Several other medical conditions and lifestyle choices can also put people at a higher risk for heart disease.")

    if add_selectbox == "Kidney Problem":
        st.title("Kidney Problem")
        st.write("A severe decrease in kidney function can lead to a buildup of toxins and impurities in the blood. This can cause people to feel tired, weak and can make it hard to concentrate. Another complication of kidney disease is anemia, which can cause weakness and fatigue. You're having trouble sleeping.")
        
        st.image('../images/streamlit_images/kidney_image.webp')

        st.title("Signs of Kidney Disease")
        st.write("1. You're more tired, have less energy or are having trouble concentrating. A severe decrease in kidney function can lead to a buildup of toxins and impurities in the blood. This can cause people to feel tired, weak and can make it hard to concentrate. Another complication of kidney disease is anemia, which can cause weakness and fatigue.")
        st.write("2. You see blood in your urine. Healthy kidneys typically keep the blood cells in the body when filtering wastes from the blood to create urine, but when the kidney's filters have been damaged, these blood cells can start to 'leak' out into the urine. In addition to signaling kidney disease, blood in the urine can be indicative of tumors, kidney stones or an infection.")
        st.write("3. Your ankles and feet are swollen. Decreased kidney function can lead to sodium retention, causing swelling in your feet and ankles. Swelling in the lower extremities can also be a sign of heart disease, liver disease and chronic leg vein problems.")
        
    

    if add_selectbox == "Diabetes":
        st.title("Diabetic")
        st.write("Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.")
        st.write("Most of the food you eat is broken down into sugar (also called glucose) and released into your bloodstream. When your blood sugar goes up, it signals your pancreas to release insulin. Insulin acts like a key to let the blood sugar into your body’s cells for use as energy.")
        st.write("If you have diabetes, your body either doesn’t make enough insulin or can’t use the insulin it makes as well as it should. When there isn’t enough insulin or cells stop responding to insulin, too much blood sugar stays in your bloodstream. Over time, that can cause serious health problems, such as heart disease, vision loss, and kidney disease.")

        st.image('../images/streamlit_images/causes_of_diabetes.jpeg', width=550)

        st.title("Types of Diabetes")
        st.subheader("Type 1 Diabetes")
        st.write("Type 1 diabetes is thought to be caused by an autoimmune reaction (the body attacks itself by mistake) that stops your body from making insulin. Approximately 5-10% of the people who have diabetes have type 1. Symptoms of type 1 diabetes often develop quickly. It’s usually diagnosed in children, teens, and young adults. If you have type 1 diabetes, you’ll need to take insulin every day to survive. Currently, no one knows how to prevent type 1 diabetes.")

        st.subheader("Type 2 Diabetes")
        st.write("With type 2 diabetes, your body doesn’t use insulin well and can’t keep blood sugar at normal levels. About 90-95% of people with diabetes have type 2. It develops over many years and is usually diagnosed in adults (but more and more in children, teens, and young adults). You may not notice any symptoms, so it’s important to get your blood sugar tested if you’re at risk. Type 2 diabetes can be prevented or delayed with healthy lifestyle changes, such as losing weight, eating healthy food, and being active.")
        
        st.subheader("Gestational Diabetes")
        st.write("Gestational diabetes develops in pregnant women who have never had diabetes. If you have gestational diabetes, your baby could be at higher risk for health problems. Gestational diabetes usually goes away after your baby is born but increases your risk for type 2 diabetes later in life. Your baby is more likely to have obesity as a child or teen, and more likely to develop type 2 diabetes later in life too.")

        st.subheader("Gestational Diabetes")
        st.write("With prediabetes, blood sugar levels are higher than normal, but not high enough yet to be diagnosed as type 2 diabetes. Prediabetes raises your risk for type 2 diabetes, heart disease, and stroke. The good news is if you have prediabetes, a CDC-recognized lifestyle change program can help you take healthy steps to reverse it")


    if add_selectbox == "Liver":
        st.title("Liver Problems")
        st.write("Liver disease can be inherited (genetic). Liver problems can also be caused by a variety of factors that damage the liver, such as viruses, alcohol use and obesity.")
        st.write("Over time, conditions that damage the liver can lead to scarring (cirrhosis), which can lead to liver failure, a life-threatening condition. But early treatment may give the liver time to heal.")

        st.image('../images/streamlit_images/labelled_liver.jpeg')
        
        st.title("Symptoms")
        st.write("1. Skin and eyes that appear yellowish (jaundice)")
        st.write("2. Abdominal pain and swelling")
        st.write("3. If the stools are pale, it may indicate a problem with the liver or other part of the biliary drainage system. Black tarry stools can happen in advanced liver disease and are caused by blood passing through the gastrointestinal tract – this needs urgent medical attention.")

    if add_selectbox == "Pneumonia":
        st.title("Pneumonia")
        st.write("Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses and fungi, can cause pneumonia.")

        st.image('../images/streamlit_images/pneumonia_image.jpeg')

        st.write("Pneumonia can range in seriousness from mild to life-threatening. It is most serious for infants and young children, people older than age 65, and people with health problems or weakened immune systems.")

        st.title("Symptopms")
        st.write("The signs and symptoms of pneumonia vary from mild to severe, depending on factors such as the type of germ causing the infection, and your age and overall health. Mild signs and symptoms often are similar to those of a cold or flu, but they last longer.")
        st.write("1. Chest pain when you breathe or cough")
        st.write("2. Lower than normal body temperature (in adults older than age 65 and people with weak immune systems)")

        st.write("Newborns and infants may not show any sign of the infection. Or they may vomit, have a fever and cough, appear restless or tired and without energy, or have difficulty breathing and eating.")

    if add_selectbox == "Malaria":
        st.title("Malaria")
        st.write("Malaria is a disease caused by a parasite. The parasite is spread to humans through the bites of infected mosquitoes. People who have malaria usually feel very sick with a high fever and shaking chills. While the disease is uncommon in temperate climates, malaria is still common in tropical and subtropical countries.")

        st.image('../images/streamlit_images/malaria_cell.jpeg')

        st.write("To reduce malaria infections, world health programs distribute preventive drugs and insecticide-treated bed nets to protect people from mosquito bites. A partially effective vaccine is being piloted in a few African countries, but there is no vaccine for travelers")
        st.write("Protective clothing, bed nets and insecticides can protect you while traveling. You also can take preventive medicine before, during and after a trip to a high-risk area. Many malaria parasites have developed resistance to common drugs used to treat the disease.")