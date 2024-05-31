import streamlit as st

st.title("Calculator")
st.write('---')
num1 = st.number_input(label='enter first number')
num2 = st.number_input(label='enter 2nd number')

st.write('Operations')
operation = st.radio('Select an operation to perform:',("Add",'Substract','multiply','divide'))
 

def calculate():
    result = 0
    if operation == 'Add':
        result = num1+num2
    elif operation == "Substract":
        result = num1-num2
    elif operation == "multiply":
        result = num1*num2
    elif operation == "divide":
        result = num1/num2
    else:
        st.warning('Number cannot be divided by zero')


    st.success(f'Answer: {result}')

if st.button('calculate'):
    calculate()