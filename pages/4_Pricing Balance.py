import streamlit as st

st.title("Pricing Balance")
st.sidebar.image("Alan-logo-green.svg")
st.write("This section should contains information about how good balance if the Pricing by product.")
st.write("Key Indicators is : ")

st.markdown("- Actual Premium/Technical Premium : This Ratio should be distributed around 100% with a normal distribution if the portfolio is priced adequately by product.")
st.image("img.png", caption="Distribution of the Ratio")

st.markdown("Technical Premium : This is the best estimate of the premium required for an individual policy to achieve the long term financial target of Alan."
            "The Technical Premium included pure technical cost and costs related to the insurance business like expenses, reinsurance, Cost of Capital, investment return.")

st.markdown("By comparing the Actual Premium with Technical Premium, this indicated how far a policy is to achieve long term financial target of Alan.")
st.markdown("This metric can be used to put in place a Renewal Stategy.")