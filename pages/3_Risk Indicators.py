import streamlit as st

st.title("Risk Indicators")
st.sidebar.image("Alan-logo-green.svg")
st.write("This section should contains information about riskiness of the portfolio")
st.write("Key Indicators are : ")

st.markdown("- Claim Frequency : numbers of claims/Exposure. This ratio indicates how many claims someone will have in a year or how long it will take on average to make a claim.  "
            "Claim frequency of 5% indicates someone will make a claim every 20 years")
st.markdown("- Claim Severity : Claim Amount/numbers of claims. This ratio indicates when a claim happen, on average how much does it cost.")
st.markdown("- Risk Premium : Frequency x Severity. This is the level of premium needed to cover the financial risk that someone in the portfolio represents. ")
st.markdown("- Distribution of log(Claims Amount) : The graph of this metric will give an idea about the homogeneity in terms of cost. If this metric has a bi-modal distribution, "
            "this indicates there are 2 very different risk in the Claim Amount and trying to build a Pricing without spliting the risk could lead to a wrong estimation.")
st.markdown("The metrics above are the basics to study before starting to model. Reporting should contains yearly evolution, also those metrics calculated by segments, risk factors. I would recommend to study the metrics separately for : ")
st.markdown("* Hospitalisation, ")
st.markdown("* Ambulatory, ")
st.markdown("* Dental")

st.markdown("Let's keep in mind if there is a subcoverage with a specific risk (like optic), this also can be study separately. ")

