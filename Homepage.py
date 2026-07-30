import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Health Portfolio Monitor",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("Health Portfolio Monitoring")

st.write("Welcome to Health Portfolio Monitoring Web App ! ")

st.markdown("The Application is made for every Alaners that would like to know learn more about the Health Portfolio. "
            "There are 5 pages that will give you a overview about the Profitability and Actuarial Drivers")

st.markdown("- ***Portfolio*** : Information about Gross Written Premium, Number of Policy, Number of insured people and their evolution")
st.markdown("- ***Observed Profitability*** : Past Loss Ratio and Combined Ratio by Accident Year, Product and Segment")
st.markdown("- ***Risk Indicator*** : Evolution of Claim Frequency, Severity and Risk Premium by Accident Year, Product and Segment")
st.markdown("- ***Pricing Balance*** : Gives you information about the Pricing Adequacy")
st.markdown("- ***Macroeconomie*** : Inflation situation, Medical Index and Consumer Price Index monitoring.")
st.markdown("- ***IBNR*** : Evolution of IBNR calculated by Reserving that should be included in Pricing")


st.sidebar.image("Alan-logo-green.svg")