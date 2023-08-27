# Import streamlit
import streamlit as st

# Get the current query parameters as a dict
params = st.experimental_get_query_params()

# Get the value of the "example" parameter, or use a default value if not set
example = params.get("example", ["0"])[0]

# Display the value of the "example" parameter
st.write(f"The current value of the 'example' parameter is {example}")

# Create a button to change the value of the "example" parameter to 1
if st.button("Set example to 1"):
    # Set the query parameter to 1
    st.experimental_set_query_params(example="1")

# Create a button to change the value of the "example" parameter to 2
if st.button("Set example to 2"):
    # Set the query parameter to 2
    st.experimental_set_query_params(example="2")

# Show different versions of the app based on the value of the "example" parameter
if example == "1":
    # Show version 1 of the app
    st.title("This is version 1 of the app")
    st.write("This version shows some cool stuff")
elif example == "2":
    # Show version 2 of the app
    st.title("This is version 2 of the app")
    st.write("This version shows some other cool stuff")
else:
    # Show a default version of the app
    st.title("This is the default version of the app")
    st.write("This version shows nothing cool")
