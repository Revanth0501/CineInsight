import streamlit as st
from PIL import Image
import json
from bs4 import BeautifulSoup
import requests,io
import sys

sys.path.append('C:/Users/revan/Desktop/Movie Recommendation/meta/Classifier.py')

from meta.Classifier import KNearestNeighbours
from urllib.request import urlopen

with open('C:/Users/revan/Desktop/Movie Recommendation/Data/movie_data.json','r+',encoding='utf-8') as f:
    data=json.load(f)

with open('C:/Users/revan/Desktop/Movie Recommendation/Data/movie_titles.json','r+',encoding='utf-8') as f:
    movie_titles =json.load(f)

with open('C:/Users/revan/Desktop/Movie Recommendation/Data/movie_details.json','r+',encoding='utf-8') as f:
    movie_details =json.load(f)

def KNN_Movie_Recommender(test_point,k):
    data1=data
    target=[0 for item in movie_titles]
    model=KNearestNeighbours(data1,target,test_point,k=k)
    
    model.fit()
    table=[]
    for i in model.indices:
        table.append([movie_titles[i][0],movie_titles[i][2],movie_details[i][0],movie_details[i][1],movie_details[i][2],data[i][-1]])
    return table

st.set_page_config(page_title='MOVIE RECOMMENDER SYSYTEM',page_icon="🎥")

def run():
    img1=Image.open('C:/Users/revan/Desktop/Movie Recommendation/361.jpg')
    img1=img1.resize((700,400),)
    st.image(img1,use_column_width=False)
    st.markdown("<h1 style='color:black;'>       Movie Recommender System</h1>", unsafe_allow_html=True)
    st.markdown('''<h4 style='text-align: left;color:#d73b5c;'>* Data is based on Top 1000 movies from imdb</h4>''', unsafe_allow_html=True)
    genres=['Action','Adventure','Animation','Biography','Comedy','Crime','Drama','Family','Fantasy','Film-Noir','History','Horror','Music','Musical','Mystery','Romance','Sci-Fi','Sport','Thriller','War','Western']
    movie=[title[0] for title in movie_titles]
    movies=sorted(movie)
    category=['Select','Movie Based','Genre Based']
    cat_op=st.selectbox('Select Recommendation Type',category)

    
    
    if cat_op ==category[0]:
        st.warning('Please Recommendation Type !!')
    
    elif cat_op==category[1]:
        select_movie=st.selectbox('Select Movie:(Recommendation will be based on this selection)',['Select']+movies)

        if select_movie=='Select':
            st.warning('Please Select Movie!!')
        else:
            no_of_records =st.slider('Select the Number you wish to Recommend From Us',min_value=5,max_value=20)
            genres=data[movies.index(select_movie)]
            test_points=genres
            table=KNN_Movie_Recommender(test_points,no_of_records+1)
            table.pop(0)
            c=0
            st.success('Some of movies from our Recommendation,have a look below')
            for movie,link,year,time,votes,ratings in table:
                c+=1
                st.markdown(f"({c})[{movie}]({link})")
                st.markdown('Year :'+str(year))
                st.markdown('Watch Time:'+str(time) +' min')
                st.markdown('Votes :'+str(votes))
                st.markdown('IMDB Rating:  '+str(ratings)+ ' out of 10.')

    else:
        sel_gen=st.multiselect('Select Genres:',genres)
        imdb_score=st.slider('Choose IMDB Score:',1,10,8)
        no_of_records=st.number_input('Number of Movies :',min_value=5,max_value=20)
        test_points=[1 if genre in sel_gen else 0 for genre in genres]
        test_points.append(imdb_score)
        table=KNN_Movie_Recommender(test_points,no_of_records)
        c=0
        st.success(' Some of the movies from our Recommendation, have a look below')
        for movie,link,year,time,votes,ratings in table:
                c+=1
               
                st.markdown(f"({c})[{movie}]({link})")
                st.markdown('Year :'+str(year))
                st.markdown('Watch Time:'+str(time) +' min')
                st.markdown('Votes :'+str(votes))
                st.markdown('IMDB Rating:  '+str(ratings)+ ' out of 10.')


if __name__ == "__main__":
    run()
