import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda():
    #pass
    st.subheader('EDA')

    yelp_df=pd.read_csv('data/review2.csv',index_col=0)
    st.dataframe(yelp_df)

    st.text('리뷰의 length를 히스토그램')
    fig1=plt.figure()
    yelp_df['length'].hist()
    st.pyplot(fig1)

    st.text('리뷰가 가장 긴 데이터')
    st.dataframe(yelp_df.loc[yelp_df['length']==yelp_df['length'].max(),])

    st.text('리뷰가 가장 짧은 데이터')
    st.dataframe(yelp_df.loc[yelp_df['length']==yelp_df['length'].min(),])

    st.text('각 별점별 리뷰의 갯수')
    my_order=yelp_df['stars'].value_counts().index
    fig2=plt.figure()
    sns.countplot(data=yelp_df, x='stars', order=my_order)
    st.pyplot(fig2)

    #리뷰의 별점을 선택하면 해당하는 별점인 데이터의 별점과 리뷰내용
    stars=sorted(yelp_df['stars'].unique())
    choice_star=st.selectbox('별점을 선택하여 리뷰 보기',stars)
    st.dataframe(yelp_df.loc[yelp_df['stars']==choice_star,['stars','text']])

