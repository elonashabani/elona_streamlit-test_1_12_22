
# "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. “  '''

import streamlit as st

#task 1:

st.title('Provimi I:')

st.text=("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

header=st.text_input('the text:',st.text)
#Declare a function called “convert_list”  that takes this string and returns a list of words from this string.(hint: you can use .split() method ). Connect this function with a button called “Return List”.When you press this button list of words is printed on streamlit. (hint: you can use st.write() )

def convert_list(text):
    lst = list(text.split())
    return lst
if st.button('Return list'):
    prnt = convert_list(st.text)
    st.write(prnt)

    
# Declare another function called “convert_upper” that takes the list from the function called “convert_list” and converts them to a list with all upper case.(hint: you need to use for loop, .upper() and .append() methods ). Connect this function to a button called “upper” that activates this function and prints te result.(hint: you need to use st.write()

def convert_upper():
    upper_list = []
    for i in convert_list(st.text):
        upper_list.append(i.upper())
    return upper_list
if st.button('Upper'):
    prnt_upper = convert_upper()
    st.write(prnt_upper)

    
   
   
   
#Declare a function called ‘count” that returns the number of elements in the list . Connect this function to a button called “print_count”. This button will print the number of elements generated from the function “count”(hint: you can use st.write)
    
def count():  
    counter = 0
    for i in convert_list(st.text):
        counter +=1
    return counter
if st.button('print_count'):
    prnt_count = count()
    st.write(prnt_count)

    
    