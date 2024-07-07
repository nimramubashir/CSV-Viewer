import streamlit as st
import pandas as pd

st.title('CSV File Uploader and Viewer')
st.write('Upload your CSV files and then click the "Upload" button for further inspection!')

uploaded_file = st.sidebar.file_uploader("Choose a file", type ='csv')

click = st.sidebar.button('Upload')
if click and uploaded_file is None:
    st.sidebar.write("No file uploaded!")
elif uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Full data", df)
    check = st.sidebar.checkbox("Display basic statistics")
    if check: 
        st.write('Basic Statistics of the file:', df.describe())

        # Display the shape of the dataframe
        st.write('Shape of the dataframe:', df.shape)

        # Display column names
        st.write('Column names:', df.columns.tolist())
    # Selectbox to choose a column to visualize
    column = st.sidebar.selectbox('Select a column to visualize', df.columns)
    
    # Display the selected column
    st.write(f'Data in the selected column - {column}:', df[column])