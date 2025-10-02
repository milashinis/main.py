import streamlit as st

# -------------------
# Page Config
# -------------------
st.set_page_config(page_title="Milashini Saravanan - Resume", layout="wide")

# -------------------
# Custom CSS for Styling
# -------------------
st.markdown(
    """
    <style>
        /* Background and text */
        .main {
            background-color: #f8f9fa;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        /* Card style */
        .card {
            background-color: #ffffff;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }
        /* Footer */
        .footer {
            text-align: center;
            color: #6c757d;
            margin-top: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------
# Title
# -------------------
st.markdown("<h1 style='text-align:center;'>📄 Milashini Saravanan</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Aspiring AI Engineer | Data & IoT Enthusiast</h3>", unsafe_allow_html=True)
st.markdown("---")

# -------------------
# Contact Info
# -------------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("📌 Contact Information")
    st.write("📧 **Email:** milashinis@gmail.com")
    st.write("📱 **Phone:** +60-104406461")
    st.write("🔗 **LinkedIn:** [linkedin.com/in/milashini](https://linkedin.com/in/milashini)")
    st.write("🌐 **GitHub:** [github.com/milashinis](https://github.com/milashinis)")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# Education
# -------------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🎓 Education")
    st.write("""
    **Bachelor of Information Technology (Artificial Intelligence)**  
    Universiti Malaysia Kelantan — *2022–2026*  
    - Focus: Artificial Intelligence, Machine Learning, Data Science  
    - Relevant coursework: Data Structures, Algorithms, Database Systems, Computer Vision
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# Experience
# -------------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("💼 Work Experience")
    st.subheader("Intern — Company Name (Jan 2026 – Jun 2026)")
    st.write("""
    - Assisted in AI model development and deployment  
    - Worked with relational databases and system integration  
    - Improved automation processes, reducing manual workload by **15%**  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# Skills
# -------------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🛠 Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.write("- Python, C++, Java")
        st.write("- Machine Learning")
    with col2:
        st.write("- Artificial Intelligence")
        st.write("- Problem Solving, Teamwork, Communication")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# Projects
# -------------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("📂 Projects")
    st.subheader("AI-Powered Course & Career Advisor")
    st.write("Developed a web app using Generative AI to guide SPM graduates in choosing degree programs and career pathways.")

    st.subheader("Smart Traffic Management System")
    st.write("Designed an IoT-based project to reduce traffic light accidents in city areas.")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# Footer
# -------------------
st.markdown("<p class='footer'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)


