import pickle
from PIL import Image

import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
from tensorflow.keras.models import load_model
import pyperclip
im = Image.open("code.ico")
st.set_page_config(page_title="Kodlama Dillerini Çevirme Uygulama", page_icon=im,initial_sidebar_state="collapsed", layout="wide")
st.markdown("""
<style>
    * {
       overflow-anchor: none !important;
       }
</style>""", unsafe_allow_html=True)

#JAVA-CS

data=pd.read_csv("data.csv")
java_texts1 = data["Java"].astype(str).tolist()
csharp_texts1 = data["CS"].astype(str).tolist()
java_tokenizer1 = Tokenizer()
java_tokenizer1.fit_on_texts(java_texts1)


csharp_tokenizer1 = Tokenizer()
csharp_tokenizer1.fit_on_texts(csharp_texts1)

java_vocab_size1 = len(java_tokenizer1.word_index) + 1
csharp_vocab_size1 = len(csharp_tokenizer1.word_index) + 1

encoder_input_sequences1 = java_tokenizer1.texts_to_sequences(java_texts1)
decoder_input_sequences1= csharp_tokenizer1.texts_to_sequences(csharp_texts1)

max_java_length = max(len(seq) for seq in encoder_input_sequences1)
max_csharp_length = max(len(seq) for seq in decoder_input_sequences1)


#CS-JAVA
java_texts2 = data["CS"].astype(str).tolist()
csharp_texts2 = data["Java"].astype(str).tolist()
java_tokenizer2 = Tokenizer()
java_tokenizer2.fit_on_texts(java_texts2)


csharp_tokenizer2 = Tokenizer()
csharp_tokenizer2.fit_on_texts(csharp_texts2)

java_vocab_size2 = len(java_tokenizer2.word_index) + 1
csharp_vocab_size2 = len(csharp_tokenizer2.word_index) + 1


encoder_input_sequences2 = java_tokenizer2.texts_to_sequences(java_texts2)
decoder_input_sequences2= csharp_tokenizer2.texts_to_sequences(csharp_texts2)


max_java_length2 = max(len(seq) for seq in encoder_input_sequences2)
max_csharp_length2 = max(len(seq) for seq in decoder_input_sequences2)

#PYTHON-CPP
data2=pd.read_csv("python-cpp.csv")
python_texts = data2["python"].astype(str).tolist()
cpp_texts = data2["cpp"].astype(str).tolist()
python_tokenizer = Tokenizer()
python_tokenizer.fit_on_texts(python_texts)


cpp_tokenizer = Tokenizer()
cpp_tokenizer.fit_on_texts(cpp_texts)
python_vocab_size = len(python_tokenizer.word_index) + 1
cpp_vocab_size = len(cpp_tokenizer.word_index) + 1


encoder_input_sequences = python_tokenizer.texts_to_sequences(python_texts)
decoder_input_sequences = cpp_tokenizer.texts_to_sequences(cpp_texts)


max_python_length = max(len(seq) for seq in encoder_input_sequences)
max_cpp_length = max(len(seq) for seq in decoder_input_sequences)

def predict_sentence(model, sentence):
    prediction = model.predict([sentence])
    return prediction[0]

java_csharp = load_model("JAVA-CS3.h5")
csharp_java=load_model("CS-JAVA5.h5")
with open("rf_cs.pkl", "rb") as file:
    model2_cs = pickle.load(file)
with open("rf_java.pkl", "rb") as file:
    model2_java= pickle.load(file)




def main():
    st.markdown("""
    <h1 style='text-align: center; color: #F1F3F2; margin-top: 2px;'>Kodlama Dillerini Çevirme Uygulaması</h1>
    """, unsafe_allow_html=True)
    html_string = """
    .stApp > header {
        background-color: transparent;
    }

    .stApp {
        margin: auto;
        font-family: "Gill Sans Extrabold", sans-serif;
        overflow: auto;

        background: #a5b5ab;
        animation: gradient 15s ease infinite;
        background-size: 400% 400%;
        background-attachment: fixed;
    }
    """

    st.markdown(f'<style>{html_string}</style>', unsafe_allow_html=True)



    with stylable_container(
            key="container_with_left",
            css_styles="""
               {
                  border-radius: 25px;
                  position: absolute;
                  top:70%;
                  left:7%;
                  padding: 40px;
                  margin-top: 40px;
                  width: 550px;
                  height: 400px;
                  background: #F1F3F2;
                  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.1);
                  overflow: hidden;
            }"""):
        st.markdown("""
        	<style>
        	.stSelectbox:first-of-type > div[data-baseweb="select"] > div {
        	            border-radius: 25px;
                          border: 1px solid #a5b5ab; /* 2 piksel kalınlığında, siyah, düz çizgi */

            	      padding: 10px;
        	}
        	</style>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            option1 = st.selectbox(key="option1",label="",
                options= ("Java", "Python", "C#","C++"),
                index=None,
                placeholder="Kaynak dili seçiniz",
            )


        with stylable_container(
                key="container_with_left_in",
                css_styles="""
                          {
                             border-radius: 25px;
                    
                             top:65%;
                             right:7%;
                             padding: 40px;
                             width: 550px;
                             height: 600px;
                             overflow: hidden;
                       }"""):

            input_text=st.text_area("Kod bloğunu giriniz:", key="code_input")
            submit_button_html = """
                            <button style="background-color: #a5b5ab; color: white; padding: 10px 20px; border: none; border-radius: 25px;">Çevir</button>"""
            translate_button = st.markdown(submit_button_html, unsafe_allow_html=True)


    with stylable_container(
            key="container_with_right",
            css_styles="""
                  {
                     border-radius: 25px;
                     position: absolute;
                     top:70%;
                     right:7%;
                      margin-top: 40px;
                     padding: 40px;
                     width: 550px;
                     height: 400px;
                     background: #F1F3F2;
                     box-shadow: 0 15px 50px rgba(0, 0, 0, 0.1);
                     overflow: hidden;
               }"""):
        col1, col2 = st.columns(2)
        with col1:
            option2 = st.selectbox(key="option2", label="",
                                   options=("Java", "Python", "C#", "C++"),
                                   index=None,
                                   placeholder="Hedef dili seçiniz",
                                   )
        with stylable_container(
                key="container_with_right_in",
                css_styles="""
                                 {
                                    border-radius: 25px;

                                    top:65%;
                                    right:7%;
                                    padding: 40px;
                                    width: 550px;
                                    height: 600px;
                                    overflow: hidden;
                              }"""):

            if option1 == "C++" and option2 == "Python":
                st.warning("Bu kaynak dilden hedef dile çevirme henüz gerçekleşmemektedir.")
            if option1 == "Java" and option2 == "Python":
                st.warning("Bu kaynak dilden hedef dile çevirme henüz gerçekleşmemektedir.")
            if option1 == "C#" and option2 == "Python":
                st.warning("Bu kaynak dilden hedef dile çevirme henüz gerçekleşmemektedir.")
            if option1 == "Java" and option2 == "C++":
                st.warning("Bu kaynak dilden hedef dile çevirme henüz gerçekleşmemektedir.")
            if option1 == "C#" and option2 == "C++":
                st.warning("Bu kaynak dilden hedef dile çevirme henüz gerçekleşmemektedir.")

            if  option1=="Java" and option2=="C#":

                if (len(input_text)>0):
                    if translate_button:
                        input_seq = java_tokenizer1.texts_to_sequences([input_text])
                        input_seq = pad_sequences(input_seq, maxlen=max_java_length, padding='post')

                        predicted_sequence = java_csharp.predict(input_seq)
                        predicted_token_ids = [np.argmax(vector) for vector in predicted_sequence[0]]

                        predicted_text = csharp_tokenizer1.sequences_to_texts([predicted_token_ids])[0]
                        prediction = predict_sentence(model2_cs, predicted_text)
                        lines = prediction.split(';')
                        lines = [line.strip() for line in lines if line.strip()]
                        formatted_code = '\n'.join(lines)
                        st.code(formatted_code, language="csharp", line_numbers=True)

            if option1 == "C#" and option2 == "Java":

                if (len(input_text) > 0) :
                    if (len(input_text)<max_csharp_length):
                        input_seq = java_tokenizer2.texts_to_sequences([input_text])
                        input_seq = pad_sequences(input_seq, maxlen=max_java_length2, padding='post')
                        predicted_sequence = csharp_java.predict(input_seq)
                        predicted_token_ids = [np.argmax(vector) for vector in predicted_sequence[0]]
                        predicted_text = csharp_tokenizer2.sequences_to_texts([predicted_token_ids])[0]
                        prediction = predict_sentence(model2_java, predicted_text)
                        lines = prediction.split(';')
                        lines = [line.strip() for line in lines if line.strip()]
                        formatted_code = '\n'.join(lines)
                        st.code(formatted_code,language="java",line_numbers=True)
                    else:
                        st.warning("Kod maksimum uzunluğa ulaştu. Lütfen çevirmek istediğiniz kod bloğunu küçültün")
            if option1 == "Python" and option2 == "C++":

                st.write("#")
                if (len(input_text) > 0):
                    st.warning("Pythondan C++ diline çevirme işlemi yakında gerçekleştirilebilecek")

if __name__ == "__main__":
    main()




