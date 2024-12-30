import streamlit as st
import functions

st.title("My Todo App")
st.subheader("Developed to learn Python")
st.write("It's my first web app")

todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo")
