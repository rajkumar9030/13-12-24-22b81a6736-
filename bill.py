import streamlit as st

sal = st.number_input("Enter the salary: ")
bill1 = st.number_input("Enter the bill 1: ")
bill2 = st.number_input("Enter the bill 2: ")
bill3 = st.number_input("Enter the bill 3: ")


sum_bills = bill1 + bill2 + bill3
st.write("Sum of bills: " + str(sum_bills))
percentage = (sum_bills / sal) * 100
st.write("Percentage of usage of salary: "+str(percentage))
