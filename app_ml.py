import streamlit as st

import joblib
import numpy as np

def run_ml():
    #pass
    st.subheader('머신러닝')
    st.subheader('문장을 입력하면, 긍정 부정 예측해 준다.')

    classifier=joblib.load('data/classifier.pkl')
    vec=joblib.load('data/vec.pkl')

    sentence=st.text_input('문장 입력')
    #유저가 입력 후 버튼을 누르면 예측하도록 한다.
    if st.button('예측 실행'):
        if sentence!='':
            new_data=np.array([sentence])
            X_new_data=vec.transform(new_data)
            X_new_data=X_new_data.toarray()
            y_pred=classifier.predict(X_new_data)

            #st.write(y_pred)
            if y_pred[0]==5:
                st.text('입력하신 문장은 긍정입니다.')
            else:
                st.text('입력하신 문장은 부정입니다.')
