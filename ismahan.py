import streamlit as st
import function


todos = function.opening_files()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("Todo App")
st.subheader("This is your todo app")
st.write("This app is to increase your productivity My Love.")


for index, todo in enumerate (todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            function.write_todos(todos)
            del st.session_state[todo]
            st.experimental_rerun()



st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
st.write("Dedicated To My Lover{ismahan}:Forever My Muse.")

