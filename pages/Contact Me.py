import streamlit as st
from PIL import Image



image = Image.open("assets/profile.jpeg")

# ---------------- HEADER ----------------
st.title("Let's Get In Touch")
st.write("Feel free to send me a message anytime.")

st.divider()

# ---------------- CONTACT INFO ----------------
st.header("Contact Information")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(image, use_container_width=True)

with col2:
    st.write("""
📧 Email: rizamelabastida05@email.com  
📱 Facebook: Rizame M. Labastida  
📞 Contact: 09XX-XXX-XXXX  
🎓 Role: Computer Science Student  
📍 Location: Mandaon, Masbate  
""")

st.divider()

# ---------------- MESSAGE FORM ----------------
st.header("Send a Quick Message")

with st.form("message_form"):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")

    with col2:
        email = st.text_input("Email Address")

    message = st.text_area("Your Message")

    submit = st.form_submit_button("Submit Message")

    if submit:
        if name and email and message:
            st.success(f"Message sent! Thank you {name} 😊")
        else:
            st.error("Please fill in all fields.")

st.divider()

st.caption("© 2026 Contact Page | Built with Streamlit")
