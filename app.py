import streamlit as st

# Page config
st.set_page_config(page_title="Milashini Saravanan - Resume", layout="wide")

# Profile section with photo and name
col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.jpg", width=150)  # Add your own photo in the same folder
with col2:
    st.title("Milashini Saravanan")
    st.write("📧 Email: your.email@example.com")
    st.write("📱 Phone: +60-123456789")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile)")
    st.write("🌐 [GitHub](https://github.com/milashinis)")

# Education
st.header("🎓 Education")
st.write("**Bachelor of Information Technology (Artificial Intelligence)** - University Name (2022–2026)")
st.write("Relevant Courses: Data Science, Machine Learning, Computer Vision")

# Work Experience
st.header("💼 Work Experience")
st.subheader("Intern - Company Name (Jan 2026 – June 2026)")
st.write("""
- Assisted in developing AI-based applications  
- Worked on database management and system integration  
- Improved process efficiency by 15% through automation
""")

# Skills
st.header("🛠 Skills")
st.write("- Python, Streamlit, SQL, FlutterFlow")
st.write("- Machine Learning, Data Visualization")
st.write("- Problem Solving, Communication, Teamwork")

# Projects
st.header("📂 Projects")
st.subheader("AI-Powered Course & Career Advisor")
st.write("Developed a web-based platform to guide SPM graduates in choosing degree programs and career paths using Generative AI.")

st.subheader("Smart Traffic Management System")
st.write("Designed IoT-based traffic light monitoring to reduce accidents in urban areas.")

# Achievements
st.header("🏆 Achievements")
st.write("- Dean’s List Award (2023, 2024)")
st.write("- Published paper on IoT crop protection system in IEEE Conference")

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
