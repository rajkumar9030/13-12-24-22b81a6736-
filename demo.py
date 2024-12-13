import streamlit as st
st.title("gross salary calculator")
basic_salary = st.number_input("Enter your basic salary:",min_value=0,step=1)
if st.button("Calculate gross salary"):
    hra=0
    da=0
    if basic_salary<10000:
        hra=basic_salary*0.67
        da=0.73*basic_salary
    elif basic_salary<20000:
        hra=basic_salary*0.69
        da = 0.76 * basic_salary
    else:
        hra=basic_salary*0.73
        da = 0.89 * basic_salary
        total_salary = hra + da + basic_salary
        st.write(total_salary)


