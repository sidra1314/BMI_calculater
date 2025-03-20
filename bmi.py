import streamlit as st

# streamlit app Title
st.title("BMI Calculater")

# User Input
weight = st.number_input("Enter your weight (kg) ",min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m) ",min_value=0.5, step=0.01)

# BMI Calculation
if st.button("calclate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        # BMI category
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi <= 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
else:
    st.error("please enter valid weight and height.")