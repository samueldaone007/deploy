import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import streamlit.components.v1 as components
import base64


def get_base64_image(path):
    with open('images1.jpg', "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
def set_bg_from_local(image_path):
    base64_img = get_base64_image(image_path)
    st.markdown(
    f"""
    <style>
   .stApp {{
            height: 100%;
            margin: 0;
            padding: 0;
        }}
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True)
    

model = joblib.load('deploy/Student_Stress_Predictor.pkl')

st.markdown('<h1 style="color:#000000;">Student Stress Predictor</h1>',unsafe_allow_html=True)
st.markdown('<p style="color:#000000; font-weight:bold; font-size:20px">Stress is a cause of many mental health and even other health issues</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#000000; font-weight:bold; font-size:20px">It is very common among students and schools need to make a batter effort to ease that stress</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#000000; font-weight:bold; font-size:20px">And with this predictor you can predict the amount of stress a student might be going through and rreach out before its TOO LATE</p>', unsafe_allow_html=True)

components.html(
    """
    <div>
       
    </div>
    """,
    height=100
)
stud_study = st.slider("How many hours does the student study per day", 1.0, 10.0,0.0)
extra = st.slider("How many Extracurricular hours per day", 1.0, 10.0,0.0)
sleep = st.slider("How many houts of sleep per day", 1.0, 10.0,0.0)
social = st.slider("How many social hours per day", 1.0, 10.0,0.0)
phy_act = st.slider("How many physical activity hours per day", 1.0, 10.0,0.0)
grades =st.slider("What are the students grades?",1.0,10.0,0.0)

features = [[stud_study, extra, sleep, social, phy_act, grades]]

if st.button("Predict Stress Level"):
    prediction = model.predict(features)[0]
    st.markdown(f"<h2 style='color:#ff0000;'>Predicted Stress Level: {prediction}</h2>", unsafe_allow_html=True)
