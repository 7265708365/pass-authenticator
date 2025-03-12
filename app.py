import streamlit as st
import re


# Develop the Application

st.set_page_config(page_title='✔Password Strength Checker')
st.title("🔒 Password Strength Checker")

password = st.text_input("Enter your password", type="password")
feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r'[A-Z]' , password) and re.search(r'[a-z]' , password):
        score += 1
    else:
        feedback.append("Password should contain both upper and lower case characters")

    if re.search(r'[0-9]' , password):
        score +=1 
    else:
        feedback.append("Password should contain at least one number")                

    if re.search(r'[@#$&*?:]' , password):
        score +=1
    else:
        feedback.append("Password should contain at least one special character")    

    if score == 4:
        feedback.append("Password is strong")
    elif score == 3:
        feedback.append("Password is medium")
    else:
        feedback.append("Password is weak")

    if feedback:    
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please enter a password to check its strength")
