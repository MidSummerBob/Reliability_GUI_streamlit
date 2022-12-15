import streamlit as st
import pandas as pd

add_sidebar = st.sidebar.selectbox("Reliability", ("Home Page", "Calculate Reliability",
                                                   "Calculate Maintenance", "Cost of Maintenance"))

if add_sidebar == "Home Page":
    header = st.container()
    feature = st.container()
    contact = st.container()

    with header:
        st.title("Welcome to our software!"
                 "\nCalculate Reliability, Maintenance and Give you Advice")

    with feature:
        st.header("Instruction of our software")
        st.text("1.How to use our software?"
                "\n2.How to calculate Reliability?"
                "\n3.How to calculate Maintenance and Cost?"
                "\n4...")

    with contact:
        st.text("Our e-mail address is: xx@python.com"
                "\nPlease feel free to contact us if you find anything to improve!")

if add_sidebar == "Calculate Reliability":
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe.head(10))

    dist_option = st.selectbox("Which distribution is this component?",
                               ("Normal", "Exponential", "Weibull", "Gamma"))
    parameter_1 = st.text_input("Insert Parameter 1", key="para1")
    parameter_2 = st.text_input("Insert Parameter 2", key="para2")
    parameter_3 = st.text_input("Insert Parameter 3", key="para3")
    if st.button("Confirm"):
        data = {
            "Distribution": [dist_option],
            "Parameter1": [parameter_1],
            "Parameter2": [parameter_2],
            "Parameter3": [parameter_3],
        }
        df = pd.DataFrame(data)
        df.to_csv("data.csv", mode="a", index=False, header=False)


    @st.cache
    def convert_df(l_df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return l_df.to_csv().encode('utf-8')

    data1 = pd.DataFrame([dist_option, parameter_1, parameter_2, parameter_3])

    csv = convert_df(data1)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='large_df.csv',
        mime='text/csv',
        disabled=True
    )

if add_sidebar == "Calculate Maintenance":
    st.write("This page is for maintenance.")

if add_sidebar == "Cost of Maintenance":
    st.write("This page is for Cost and Advice.")
