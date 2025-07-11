import streamlit as st
import smtplib
import ssl
from email.message import EmailMessage

st.set_page_config(page_title="📧 Email Sender", page_icon="📨")

st.title("📧 Send an Email via Python + Streamlit")

# Email credentials input
sender_email = st.text_input("Sender Email Address")
sender_password = st.text_input("Sender Email Password", type="password")
receiver_email = st.text_input("Receiver Email Address")

subject = st.text_input("Email Subject")
message_body = st.text_area("Email Body")

if st.button("Send Email"):
    if not sender_email or not sender_password or not receiver_email or not message_body:
        st.warning("Please fill all fields before sending.")
    else:
        try:
            # Compose email
            msg = EmailMessage()
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg["Subject"] = subject
            msg.set_content(message_body)

            # Send email using Gmail SMTP (or similar)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, sender_password)
                server.send_message(msg)

            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
