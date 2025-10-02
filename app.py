import streamlit as st

# -------------------
# Page Title
# -------------------
st.set_page_config(page_title="Milashini Saravanan - Resume", layout="wide")
st.title("📄 Milashini Saravanan's Resume")

# -------------------
# Contact Information
# -------------------
st.header("📌 Contact Information")
st.write("📧 **Email:** milashinis@gmail.com")
st.write("📱 **Phone:** +60-104406461")
st.write("🔗 **LinkedIn:** [linkedin.com/in/milashini](https://linkedin.com/in/milashini)")
st.write("🌐 **GitHub:** [github.com/milashinis](https://github.com/milashinis)")

st.markdown("---")

# -------------------
# Education
# -------------------
st.header("🎓 Education")
st.write("""
**Bachelor of Information Technology (Artificial Intelligence)**  
Universiti Malaysia Kelantan — *2022–2026*  
- Focus: Artificial Intelligence, Machine Learning, Data Science  
- Relevant coursework: Data Structures, Algorithms, Database Systems, Computer Vision
""")

st.markdown("---")

# -------------------
# Work Experience
# -------------------
st.header("💼 Work Experience")
st.subheader("Intern — Company Name (Jan 2026 – Jun 2026)")
st.write("""
- Assisted in AI model development and deployment  
- Worked with relational databases and system integration  
- Improved automation processes, reducing manual workload by **15%**  
""")

st.markdown("---")

# -------------------
# Skills
# -------------------
st.header("🛠 Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("- Python, C++, Java")
    st.write("- Machine Learning")
with col2:
    st.write("- Artificial Intelligence")
    st.write("- Problem Solving, Teamwork, Communication")

st.markdown("---")

# -------------------
# Projects & Achievements
# -------------------
st.header("📂 Projects & Achievements")
st.subheader("AI-Powered Course & Career Advisor")
st.write("Developed a web app using Generative AI to guide SPM graduates in choosing degree programs and career pathways.")

st.subheader("Smart Traffic Management System")
st.write("Designed an IoT-based project to reduce traffic light accidents in city areas.")

st.subheader("Achievements")
st.write("- 🏆 Dean’s List Award (2023, 2024)")

st.markdown("---")

# -------------------
# Footer
# -------------------
st.markdown("<p style='text-align:center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)

