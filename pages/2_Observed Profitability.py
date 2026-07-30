import streamlit as st

st.title("Observed Profitability")

st.write("This section should contains information about profitability")
st.write("Key Indicators are : ")

st.markdown("- Loss Ratio : Claim Amount / Earned Premium. This gives you, by accident year, how much the earned premium  covers claim. ")

st.markdown("- Ultimate Loss Ratio : (Claim Amount + IBNR) / Earned Premium. Same as Loss Ratio, but for open claims, the claim amount can change over time. "
            "Without IBNR, recent years Loss Ratio can be underestimated. Healthcare business is known to be short term in terms of claims development.")

st.markdown("- Combined Ratio : Loss Ratio + Expenses Ratio. Expenses Ratio gives you the cost of underwriting additional euro. ")
st.markdown("- Ultimate Combined Ratio : Ultimate Loss Ratio + Expenses Ratio. Same as CoR but including IBNR.")

st.markdown("Indicators described above should be calculated by accident year, also by segment, product and risk factors.")
st.markdown("Also, it is important to keep in mind past performance does not reflect future performance. Those are important metrics to explain and understand the past but does not have predictive power !")