import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Data Decoded",
    page_icon=":bar_chart:",
    layout="wide",
)

# Title and header with custom styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&family=Montserrat:wght@400;700&family=Nunito:wght@400;700&family=Poppins:wght@400;700&family=Ubuntu:wght@400;700&display=swap');

        h1{
            color: #FF4444 ;
            font-family: Ubuntu, sans-serif;
        }
        h3 {
            color: #696969;
            font-family: 'Arial';
        }
    </style>
""", unsafe_allow_html=True)

# Title and header
st.markdown("<h1>Data Decoded</h1>", unsafe_allow_html=True)
st.markdown("<h3>Explore Our Analysis projects</h3>", unsafe_allow_html=True)


# Description
st.markdown("""
Welcome to our hub where you can find various analysis projects and models we've developed. Click on any project name to explore further.
""")

# List of Streamlit apps with more styling
apps = [
    {"name": "IPL Orange Cap Analysis", "link": "https://ipl-orange-cap.streamlit.app/", "description": "This app does amazing things with data."},
    
    # Add more apps as needed
]

# Function to display app information
def display_app_info(app):
    st.markdown(f"### [{app['name']}]({app['link']})")
    st.markdown(f"*{app['description']}*")
    st.markdown("---")

# Display each app with more styling
for app in apps:
    display_app_info(app)

# Footer with contact information and social media icons
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 88%;
            background-color: transparent;
            color: #FF4444;
            text-align: center;
             /* Add padding on left and right sides */
            font-size: 15px;
            box-sizing: border-box; /* Ensure padding and width are accounted for correctly */
        }
        .footer-content {
            size:2px,
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px; /* Adjust max-width as needed */
            margin: 0 auto;
            padding: 10px 20px;
        }
        .footer a {
            color: #333;
            text-decoration: none;
            margin: 0 10px;
        }
        .footer a:hover {
            color: #007BFF;
        }
        .footer-icons {
            margin-top: 5px;
        }
        .footer-icons img {
            width: 20px;
            height: 20px;
            margin: 0 5px;
            vertical-align: middle;
        }
    </style>
    <div class="footer">
        <div class="footer-content">
            <div style='font-family: Arial, sans-serif;'>Developed by Bhavik Rohit | Contact: bhavikrohit22@gmail.com</div>
            <div class="footer-icons">
                <a href="https://github.com/Bhavik2209" target="_blank"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/github.svg" alt="GitHub"></a>
                <a href="https://linkedin.com/in/bhavik-rohit" target="_blank"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/linkedin.svg" alt="LinkedIn"></a>
                <a href="https://x.com/BhavikRohit22" target="_blank"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/twitter.svg" alt="Twitter"></a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
