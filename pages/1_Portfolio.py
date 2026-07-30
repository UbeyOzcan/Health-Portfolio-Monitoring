import streamlit as st

st.title("Portfolio")

st.write("This section should contains information about the portfolio")
st.write("Key Indicators are : ")
st.markdown("- GWP : Gross Written Premium indicate the total volume of Premium underwritten by Month."
            "Also, some this metric should study by product, by segment and by risk factors (Age, type of job, type of company, region, NACE Code, etc ..)"
            "Moreover, GWP has to be monitor by type of policy : Part of GWP from New Business and Renewals")

st.markdown("- Number of policies : on monthly basis, the number of policies that are renewed, newly underwritten and lapsed. "
            "Renewals + New Business - Lapses = Net Position in terms of Policies my month."
            "This indicator is helpful to monitor if the Business Plan ongoing well or not based on this evolution.")
