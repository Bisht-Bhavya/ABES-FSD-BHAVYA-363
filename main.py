import streamlit as st
st.title("Streamlit Tutorial")
st.write("Hello")
st.header("header")
st.subheader("sub header")
st.divider()
st.code("#include<iostream>")
st.divider()
code = '''
def add(a,b)
  return a+b
'''
st.code(code, language="python")
st.caption("This is a caption")
st.button("Click me")
st.checkbox("I agree")
st.radio("Choose one", ("Option 1", "Option 2", "Option 3"))
st.selectbox("Select an option", ("Option A", "Option B", "Option C"))
st.multiselect("Select multiple options", ("Option X", "Option Y", "Option Z"))
st.slider("Select a value", 0, 100, 50)
st.select_slider("Select a value", ["Low", "Medium", "High"]) 
st.image('lol.jfif')
st.caption("This is an image")
i=st.text_area("Enter some text")
t = st.text_input("Enter something")
color = st.color_picker("Pick a color")
enable =st.toggle("Enable feature")
picture = st.camera_input("Take a picture",disabled=enable)
if picture:
    st.image(picture)
if enable:
    st.write("Feature enabled")
st.logo('Screenshot 2026-03-13 004458.png',size='large')
btn = st.button("Submit", type='primary') 
if btn:
    st.write("button clicked")
st.button("Cancel", type='secondary') 
st.button("Delete", type='tertiary')
st.divider()
st.markdown("This is **markdown** text with *emphasis* and a [link](https://www.google.com).")
if i:
    st.write(i)

