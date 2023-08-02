import streamlit as st
import requests
import webbrowser

# Title
st.title("API Testing")

# type input
typeInput = st.text_input("Enter type: ")

# destination input
destinationInput = st.text_input("Enter destination: ")

# Submit button
if typeInput and destinationInput:
    if st.button("Submit"):
        st.write("You submitted: ", typeInput, " and ", destinationInput)

# endpoint
url = "https://dummyjson.com/products/1"

# API call
response = requests.get(url)
data = response.json()

# Display API data
if response.status_code == 200 and data:
    if st.button("Open in New Tab"):
        webbrowser.open_new_tab(url)


# ---------------- POST request ------------------
# data
# data = {
#     "key1": "value1",
#     "key2": "value2"
# }

# POST request
# response = requests.post(url, data=data)

# # Check the response status code
# if response.status_code == 200:
#     # Request was successful
#     st.write("POST request was successful!")
#     st.write("Response content:", response.json())
# else:
#     # Request failed
#     st.write("POST request failed with status code:", response.status_code )





