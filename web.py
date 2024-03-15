import streamlit as st
import Modules.functions as functions

current_todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    current_todos.append(todo + "\n")
    functions.write_todos(current_todos)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is the subheader")
st.write("This app is to increase productivity")


for index, todos in enumerate(current_todos):
    todos = todos.strip("\n")
    checkbox = st.checkbox(todos, key=todos)
    if checkbox:
        current_todos.pop(index)
        functions.write_todos(current_todos)
        st.rerun()

st.text_input(label="input", label_visibility="hidden", placeholder="Enter a new todo",
              on_change=add_todo, key="new_todo")