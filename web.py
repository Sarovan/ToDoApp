import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("Developed to learn Python")
st.write("It's my first web app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo", on_change=add_todo, key="new_todo")

st.session_state
