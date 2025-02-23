import streamlit as st

# 🎨 Page Configuration
st.set_page_config(page_title="Car Web App", page_icon="🚗", layout="wide")

# 🎨 Custom Styling for Title (Bigger & More Stylish)
st.markdown(
    """
    <h1 style='text-align: center; font-size: 80px; font-weight: bold;'>
        <span style='color: purple;'>🚗 Car Info</span> 
        <span style='color: grey;'>Web App</span>
    </h1>
    """,
    unsafe_allow_html=True
)

# 📌 Car Name Input (Bigger Font)
st.markdown(
    "<h3 style='color: purple; font-size: 30px;'>🔍 Enter Car Name</h3>", 
    unsafe_allow_html=True
)
car_name = st.text_input("", "Tesla Model S", key="car_name", help="Type car name here", max_chars=30)

# 🧄 Ensure image file is correctly referenced
car_image_path = "patric.jpg"

# 🚗 Dummy Car Data (Tesla Model S Full Info)
car_data = {
    "Tesla Model S": {
        "model": "Tesla Model S",
        "manufacturer": "Tesla, Inc.",
        "origin_country": "United States",
        "price": "$80,000",
        "engine": "Electric Motor (No CC, Battery Powered)",
        "top_speed": "200 mph (322 km/h)",
        "acceleration": "0-60 mph in 2.4 seconds",
        "range": "396 miles (637 km) per charge",
        "seating_capacity": "5 Adults",
        "comfort_features": [
            "✅ Heated & Cooled Leather Seats",
            "1.1 Ultra-soft premium material for long journeys",
            "✅ 17-inch Touchscreen Display",
            "1.1 Advanced infotainment & navigation system",
            "✅ Auto Climate Control",
            "1.1 Adjusts temperature automatically for max comfort"
        ],
        "safety_features": [
            "✅ Autopilot with Full Self-Driving",
            "1.1 Advanced AI-based driving assistance",
            "✅ 360° Camera & Sensors",
            "1.1 Provides complete visibility & collision alerts",
            "✅ Emergency Braking System",
            "1.1 Detects obstacles & applies automatic brakes"
        ],
        "image": car_image_path  # Local image reference
    }
}

# 🔍 Fetch Car Data
car_info = car_data.get(car_name, None)

if car_info:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # 🧄 Display Car Image
        st.image(car_info["image"], caption=car_info["model"], use_container_width=True)
    
    with col2:
        # 💋 Car Details (Stylish Look)
        st.markdown(
            "<h2 style='color: purple; font-size: 28px;'>🚘 Car Details</h2>", 
            unsafe_allow_html=True
        )
        st.markdown(f"<p style='font-size: 20px;'><strong>Model:</strong> {car_info['model']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px;'><strong>Manufacturer:</strong> {car_info['manufacturer']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px;'><strong>Country of Origin:</strong> {car_info['origin_country']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px;'><strong>Price:</strong> {car_info['price']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px;'><strong>Engine:</strong> {car_info['engine']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px;'><strong>Top Speed:</strong> {car_info['top_speed']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px;'><strong>Acceleration:</strong> {car_info['acceleration']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px;'><strong>Battery Range:</strong> {car_info['range']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px;'><strong>Seating Capacity:</strong> {car_info['seating_capacity']}</p>", unsafe_allow_html=True)

    # ✨ Comfort Features Section
    st.markdown("<h3 style='color: purple; font-size: 24px;'>🧛‍♂️ Comfort Features:</h3>", unsafe_allow_html=True)
    for feature in car_info["comfort_features"]:
        st.markdown(f"<p style='font-size: 18px; color: grey;'> {feature}</p>", unsafe_allow_html=True)

    # 🛡️ Safety Features Section
    st.markdown("<h3 style='color: purple; font-size: 24px;'>🛡️ Safety Features:</h3>", unsafe_allow_html=True)
    for feature in car_info["safety_features"]:
        st.markdown(f"<p style='font-size: 18px; color: grey;'> {feature}</p>", unsafe_allow_html=True)

    # 🔘 Toggle for Contact Info
    if st.toggle("📩 Show Contact Info"):
        st.markdown("<h3 style='color: purple; font-size: 24px;'>📞 Contact Information:</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>📞 <strong>Contact:</strong> +1-234-567-890</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>📧 <strong>Email:</strong> info@carshop.com</p>", unsafe_allow_html=True)
else:
    st.error("🚨 Car not found! Please enter a valid car name.")
