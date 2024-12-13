import streamlit as st
st.title('Certificate generation')
project_score=st.number_input("enter the project score :")
internal_score=st.number_input("enter the internal score :")
external_score=st.number_input("enter the external score :")
if project_score<50:
    st.write("invalid project score :"+str(project_score))
elif internal_score<50:
   st.write("invalid internal score :"+str(internal_score))
elif(external_score<50):
    st.write("invalid external score :"+str(external_score))
else:
    total_score=0.7*project_score+0.1*internal_score+0.2*external_score
    if(total_score>90):
        st.write(" A grade")
    elif(total_score>80):
        st.write("B grade")
    else:
        st.write("c grade")




