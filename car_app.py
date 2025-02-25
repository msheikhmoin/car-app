import streamlit as st
import os

# Page Configuration
st.set_page_config(page_title="Car Web App", page_icon="🚗", layout="wide")

# Toggle Button for Contact Info
with st.sidebar:
    show_contact = st.checkbox("Show Contact Info")
    if show_contact:
        st.markdown("""
        **👤 Contact Information:**
        - **Email:** support@carinfo.com
        - **Phone:** +1 234 567 8900
        """)

# Title
st.markdown(
    """
    <h1 style='text-align: center; font-size: 100px; font-weight: bold;'>
        <span style='color: red;'>🚗 Car </span> 
        <span style='color: red;'>Web App</span>
    </h1>
    """,
    unsafe_allow_html=True
)

# **GitHub Base URL for Images**
GITHUB_BASE_URL = "https://raw.githubusercontent.com/msheikhmoin/car-app/main/car_app/"

# **Car Data Dictionary**
car_data = {
    "Tesla Model S": {
        "manufacturer": "Tesla, Inc.",
        "origin_country": "United States",
        "price": "$80,000",
        "engine": "Electric Motor (Battery Powered)",
        "top_speed": "200 mph (322 km/h)",
        "acceleration": "0-60 mph in 2.4 seconds",
        "range": "396 miles (637 km) per charge",
        "seating_capacity": "5 Adults",
        "features": ["Autopilot", "Glass Roof", "Wireless Charging", "Premium Sound System"],
        "safety_features": ["Automatic Emergency Braking", "Lane Keeping Assist", "Collision Warning"],
        "image": "patric.jpg"
    },
    "BMW i8": {
        "manufacturer": "BMW",
        "origin_country": "Germany",
        "price": "$147,500",
        "engine": "1.5L Turbo Hybrid + Electric Motor",
        "top_speed": "155 mph (250 km/h)",
        "acceleration": "0-60 mph in 4.2 seconds",
        "range": "330 miles (531 km) per charge",
        "seating_capacity": "4 Adults",
        "features": ["Scissor Doors", "Carbon Fiber Body", "HUD Display", "Gesture Control"],
        "safety_features": ["ABS Brakes", "Lane Departure Warning", "Adaptive Headlights"],
        "image": "bmw-i8.jpg"
    },
    "Audi e-tron GT": {
        "manufacturer": "Audi AG",
        "origin_country": "Germany",
        "price": "$99,900",
        "engine": "Dual Electric Motors (AWD)",
        "top_speed": "152 mph (245 km/h)",
        "acceleration": "0-60 mph in 3.9 seconds",
        "range": "238 miles (383 km) per charge",
        "seating_capacity": "5 Adults",
        "features": ["Matrix LED Headlights", "Quattro AWD System", "Sports Seats", "Bang & Olufsen Sound"],
        "safety_features": ["Traffic Sign Recognition", "Night Vision Assist", "Side Assist"],
        "image": "audi-e-tron-gt.jpg"
    }
}

# **Car Selection Dropdown**
selected_car = st.selectbox("Select a Car", list(car_data.keys()))

# **Display Selected Car Information**
if selected_car:
    car_info = car_data[selected_car]
    st.markdown(f"""
    <h3 style="color: red;">🚗 {car_info['manufacturer']} - {car_info['origin_country']}</h3>
    """, unsafe_allow_html=True)

    # **Fix: Correct Image URL**
    image_url = f"{GITHUB_BASE_URL}{car_info['image']}"
    st.image(image_url, caption=selected_car, use_container_width=True)

    # **Car Details**
    st.write(f"💰 **Price:** {car_info['price']}")
    st.write(f"⚡ **Engine:** {car_info['engine']}")
    st.write(f"🚀 **Top Speed:** {car_info['top_speed']}")
    st.write(f"⏱ **Acceleration:** {car_info['acceleration']}")
    st.write(f"🔋 **Battery Range:** {car_info['range']}")
    st.write(f"🛋️ **Seating Capacity:** {car_info['seating_capacity']}")

    # **Features Section**
    st.markdown("<h4 style='color: red;'>🚀 Features</h4>", unsafe_allow_html=True)
    st.write(", ".join(car_info['features']))

    # **Safety Features Section**
    st.markdown("<h4 style='color: red;'>🛡️ Safety Features</h4>", unsafe_allow_html=True)
    st.write(", ".join(car_info['safety_features']))
