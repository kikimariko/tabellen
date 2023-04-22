import streamlit as st

# with st.form("my_form"):
#    st.write("Inside the form")
#    age = st.text_input("Age")
#
#    # Every form must have a submit button.
#    submitted = st.form_submit_button("Submit")
#    if submitted:
#        st.write("Je bent {} jaar oud.".format(age))
#
# st.write("Outside the form")

# def nieuwe_klant_form():
#     with st.form("Nieuwe klant"):
#         achternaam = st.text_input("achternaam")
#         submitted = st.form_submit_button("Submit")
#         if submitted:
#             st.success("Teogevoegd.")
#
# nieuwe_klant_form()

with st.form(key='my-form', clear_on_submit=True):
    name = st.text_input('Enter your name')
    submit = st.form_submit_button('Submit')

st.write('Press submit to have your name printed below')

if submit:
    st.write(f'hello {name}')