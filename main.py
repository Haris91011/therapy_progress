import streamlit as st
import requests
from streamlit_chat import message

# Streamlit UI to upload multiple files
st.markdown("""
    <style>
    .title {
        font-size: xx-large;
        font-weight: bold;
        text-align: center;
    }
    </style>
    <div class="title">Therapy Progress Application</div>
""", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center">
        Upload therapy session text files to track the progress over time.
    </div>
""", unsafe_allow_html=True)

uploaded_files = st.file_uploader("Choose .txt files", type="txt", accept_multiple_files=True)

if uploaded_files:
    st.write(f"{len(uploaded_files)} files uploaded.")

    # Button to submit the files
    if st.button("Generate Progress"):
        # Prepare files to send to FastAPI backend
        files_to_send = [("files", (uploaded_file.name, uploaded_file, "text/plain")) for uploaded_file in uploaded_files]
        
        # FastAPI endpoint URL (update with your actual API URL if hosted remotely)
        url = "https://mentalyc-542808340038.us-central1.run.app/generate-progress"  # Adjust to match your backend URL
        
        try:
            # POST request to FastAPI
            response = requests.post(url, files=files_to_send)

            # Handle successful response
            if response.status_code == 200:
                result = response.json()
                st.success("Progress successfully generated!")
                message(result['data']['progress']) # Display the response from FastAPI
            else:
                st.error(f"Error: {response.status_code}, {response.text}")
        except Exception as e:
            st.error(f"An error occurred : {e}")


