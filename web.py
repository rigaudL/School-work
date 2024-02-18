import functions_for_todo as func
import streamlit as st

'''
create front end
add functions
and connnect backend

'''
item_removed = False
todo_from_database_as_list = func.read_todos_from_file()

def add_todo():
    to_do_value_frominputtext = st.session_state['new_todo'] + "\n"
    todo_from_database_as_list.append(to_do_value_frominputtext)
    func.write_todos_to_file(todo_from_database_as_list)



st.title("My first Streamlit app")
st.subheader("My todo to help me work better")
st.write("TO - DO")

for index, each_todo in enumerate(todo_from_database_as_list):
    checkbox =  st.checkbox(each_todo, key= index)
if checkbox :
    todo_from_database_as_list.pop(index) 
    func.write_todos_to_file(todo_from_database_as_list)

        
        
st.text_input(label="" ,placeholder= "Add a new todo" , on_change = add_todo, key= "new_todo" )
'''
below is the session state and the key is from the text_input button aka the part im typeing stuff n enter on
and the value is what i entered in that field and press enter
''' 
st.session_state 