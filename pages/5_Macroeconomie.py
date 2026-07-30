import streamlit as st

st.title("Portfolio")
st.sidebar.image("Alan-logo-green.svg")
st.write("This section should contains information about the country macroeconomics situation.")
st.write("Key Indicators are : ")

st.markdown("- Medical Index : Publish on yearly basis (1st of July). This index can be used as maximum indexing of premium or deductibles. "
            "To apply the Medical Index, 2 conditions should be fulfilled : possible indexing in the clause of contract and medical index higher than consumer price index")

st.markdown("- The Consumer Price Index (CPI) is a key economic indicator that measures price changes over time for a representative basket of consumer goods and services, tracking inflation and shifts in household living costs. "
            "This index can be found by group of goods and services at more granular level.")

st.markdown("- EIOPA Risk Free Rate : Interest Rate Market has an inverse-reactive relationship with inflation meaning central banks typically raise interest rates to cool down high inflation, and lower rates to stimulate a sluggish economy. Generally, they move in the same direction over time because rising inflation prompts central banks to hike rates, reducing consumer demand and stabilizing prices.")
