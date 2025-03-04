import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄")

# Title of the app
st.title("✨ Stylish Unit Converter 🔄")

# Converter selection
st.sidebar.header("Select Conversion Type")
conversion_type = st.sidebar.radio(
    "Choose conversion category:",
    ("Length", "Weight", "Temperature", "Volume")
)

# Function to handle length conversions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
    }
    result = value * length_units[from_unit] / length_units[to_unit]
    return result

# Function to handle weight conversions
def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    result = value * weight_units[from_unit] / weight_units[to_unit]
    return result

# Function to handle temperature conversions
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Function to handle volume conversions
def convert_volume(value, from_unit, to_unit):
    volume_units = {
        "Liters": 1,
        "Milliliters": 1000,
        "Cubic Meters": 0.001,
        "Gallons": 0.264172,
        "Quarts": 1.05669,
        "Pints": 2.11338,
        "Cups": 4.22675,
    }
    result = value * volume_units[from_unit] / volume_units[to_unit]
    return result

# Handling conversions based on selected category
if conversion_type == "Length":
    st.header("📏 Length Converter")
    value = st.number_input("Enter value to convert:", min_value=0.0, step=0.1)
    from_unit = st.selectbox("From unit:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet"])
    to_unit = st.selectbox("To unit:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet"])
    
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Weight":
    st.header("⚖️ Weight Converter")
    value = st.number_input("Enter value to convert:", min_value=0.0, step=0.1)
    from_unit = st.selectbox("From unit:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To unit:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Temperature":
    st.header("🌡️ Temperature Converter")
    value = st.number_input("Enter value to convert:", min_value=-273.15, step=0.1)
    from_unit = st.selectbox("From unit:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To unit:", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value}° {from_unit} = {result:.2f}° {to_unit}")

elif conversion_type == "Volume":
    st.header("💧 Volume Converter")
    value = st.number_input("Enter value to convert:", min_value=0.0, step=0.1)
    from_unit = st.selectbox("From unit:", ["Liters", "Milliliters", "Cubic Meters", "Gallons", "Quarts", "Pints", "Cups"])
    to_unit = st.selectbox("To unit:", ["Liters", "Milliliters", "Cubic Meters", "Gallons", "Quarts", "Pints", "Cups"])
    
    if st.button("Convert"):
        result = convert_volume(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

# Footer section
st.write("-" * 50)
st.write("🛠️ Created with 💖 by Ashii Malik | **Unit Converter** ✨")
