import streamlit as st

def main():
    st.title("Simple Calculator")
    
    # Create a clean layout with columns
    col1, col2 = st.columns(2)
    
    # Input fields
    with col1:
        num1 = st.number_input("Enter first number", step=1.0)
    with col2:
        num2 = st.number_input("Enter second number", step=1.0)
    
    # Operation buttons in a grid layout
    col3, col4, col5, col6 = st.columns(4)
    
    with col3:
        add = st.button("Add (+)")
    with col4:
        subtract = st.button("Subtract (-)")
    with col5:
        multiply = st.button("Multiply (×)")
    with col6:
        divide = st.button("Divide (÷)")
    
    # Result calculation
    if add:
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    
    elif subtract:
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    
    elif multiply:
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    
    elif divide:
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("Error: Division by zero is not allowed!")

    # Add some styling
    st.markdown("""
    <style>
        div.stButton > button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            padding: 10px;
        }
        div.stButton > button:hover {
            background-color: #45a049;
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()