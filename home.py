import streamlit as st
from PIL import Image


#image=Image.open(r"C:\Users\ADMIN\Downloads\feature-beth-blog-feb2022.jpg")
#st.image(Image)

def home_page():
    st.write("Telco Churn Classification Project")

    st.markdown(""" This uses machine learning to classify whether a customer is likely to churn or not""")
    st.subheader("Instructions")
    st.markdown("""
                - Upload a csv file
                - Select the features for classification
                - Choose a machine learning model from the dropdown
                - Click on'Classify' to get the predicted results
                - The app gives you a report on the performance of the model
                - Expect it to give metrics like f1 score, recall, precision and accuracy
                """)

    st.header("App Features")
    st.markdown("""
                - **Data View**:Access the customer data.
                - **Predict View**:Shows the various models and predictions you will make.
                - **Dashboard**:Show data visualizations for insights.
                """)
    
    st.subheader("User Benefits")
    st.markdown("""
                - **Data Driven Decisions**:You make an informed decison.
                - **Access Machine Learning**:Utilize machine learning
                """)
    
    st.write("### How to Run the application")
    with st.container(border=True):
        st.code("""
                # Activate the virtual environment
                env/scripts/activate
                
                # Run the App
                streamlit run p.py
                        """)
        
    # adding embedded link
    st.video("https://www.youtube.com/watch?v=ocMd2loRfWE, autoplay=True")

    # adding clickable link
    st.markdown("[Watch a Demo](https://www.youtube.com/watch?v=ocMd2loRfWE)")
    
    #adding an image/method 1
    #st.image(r"C:\Users\ADMIN\Downloads\download.jpg")

    #adding an image/method 2
    #install pillow -- from PIL import Image
    #image=Image.open(r"C:\Users\ADMIN\Downloads\feature-beth-blog-feb2022.jpg")
    #st.image(Image)

    st.divider()
    st.write("====" * 15)

    st.write("Need Help?")
    st.write("Contact me on: https://github.com/2Patty")