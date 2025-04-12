import streamlit as st
from langflow_chain import analyze_scholarship_eligibility

st.title("Scholarship Eligibility Analyzer")

with st.form("eligibility_form"):
    name = st.text_input("Name")
    gpa = st.text_input("GPA (out of 100)")
    income = st.number_input("Family Annual Income (in LPA)", step=0.1)
    academic_level = st.text_input("Academic Level (e.g., 12th, undergraduate)")
    gender = st.selectbox("Gender", ["", "Male", "Female", "Other"])
    interests = st.text_area("Interests (comma-separated, e.g., engineering, sports, stem)")

    submitted = st.form_submit_button("Analyze Eligibility")

    if submitted:
        student_info = {
            "name": name,
            "gpa": gpa,
            "income": income,
            "academic_level": academic_level,
            "gender": gender,
            "interests": interests
        }

        with st.spinner("Analyzing..."):
            result = analyze_scholarship_eligibility(student_info)

        st.subheader("Entered Information")
        st.json(student_info)

        st.subheader("Eligibility Assessment")
        st.write(result['assessment'])

        st.subheader("Potential Scholarships")
        if result['scholarships']:
            for scholarship in result['scholarships']:
                st.markdown(f"**{scholarship['name']}**: {scholarship['description']}")
        else:
            st.write("No matching scholarships found.")

        st.subheader("Application Guidance")
        st.write(result['guidance'])
