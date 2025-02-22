Healthy Diet & Workout Planner

📌 Overview

The Healthy Diet & Workout Planner is a web-based application built using Streamlit. This app helps users calculate their BMI (Body Mass Index) based on their weight and height and provides personalized diet and workout recommendations accordingly. Additionally, it suggests daily water intake for better hydration.

🛠 Technologies Used

Python (Primary language)

Streamlit (For UI development)

HTML & CSS (For styling custom elements)

Datetime Module (To handle date-related functionalities)

Markdown & Streamlit Widgets (For user interaction and visual representation)

🚀 Features

BMI Calculator: Computes BMI using weight and height inputs.

Personalized Diet Plan: Recommends diet based on BMI category.

Workout Recommendations: Suggests exercises according to BMI.

Water Intake Guide: Estimates daily water consumption based on weight.

Responsive & User-Friendly UI: Developed using Streamlit components and custom CSS.

📂 Project Setup

1️⃣ Prerequisites

Ensure you have Python 3.7+ installed on your system.

2️⃣ Installation Steps

# Clone this repository
git clone https://github.com/Shabnamwahid/streamlit-python-assgnment.git
cd streamlit-python-assgnment

# Create a virtual environment (Optional but recommended)
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows

# Install required dependencies
pip install -r requirements.txt

3️⃣ Run the Application

streamlit run app.py

📝 Code Explanation

1️⃣ Setting up Streamlit Configuration

st.set_page_config(page_title="Healthy Diet & Workout Planner", layout="centered", initial_sidebar_state="collapsed")

Sets the page title, layout, and sidebar settings.

2️⃣ Applying Custom CSS

st.markdown(
    """
    <style>
    .title-heading {
        background-image: url("image_link_here");
        background-size: cover;
        padding: 30px;
        text-align: center;
        color: white;
        font-size: 36px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

Uses HTML & CSS inside Streamlit to style headings with background images.

3️⃣ BMI Calculation Function

def calculate_bmi(weight, height_m):
    return round(weight / (height_m ** 2), 2)

This function calculates BMI using the standard formula:

BMI = weight (kg) / height (m²)

4️⃣ Generating Diet & Workout Plans

def get_diet_plan(bmi):
    if bmi < 18.5:
        return "High-protein diet with healthy fats."
    elif 18.5 <= bmi < 24.9:
        return "Balanced diet with vegetables and whole grains."
    elif 25 <= bmi < 29.9:
        return "Low-carb diet with lean proteins."
    else:
        return "Strict diet, more fiber, avoid sugar & junk food."

Based on BMI value, it suggests a suitable diet.

def get_workout_plan(bmi):
    if bmi < 18.5:
        return "Light strength training and yoga."
    elif 18.5 <= bmi < 24.9:
        return "Regular cardio, weight training, and flexibility exercises."
    elif 25 <= bmi < 29.9:
        return "High-intensity interval training (HIIT)."
    else:
        return "Low-impact cardio like swimming and walking."

Similar to the diet function, this provides an exercise plan based on BMI.

5️⃣ Main Application Logic

def main():
    name = st.text_input("Enter Your Name")
    age = st.number_input("Enter Your Age", min_value=10, max_value=100, step=1)
    weight = st.number_input("Enter Your Weight (kg)", min_value=20, max_value=200, step=1)
    feet = st.number_input("Enter Height (Feet)", min_value=3, max_value=7, step=1)
    inches = st.number_input("Enter Height (Inches)", min_value=0, max_value=11, step=1)
    
    height_m = ((feet * 12) + inches) * 0.0254  # Convert feet & inches to meters
    
    if st.button("Calculate BMI & Get Plan"):
        if weight and height_m:
            bmi = calculate_bmi(weight, height_m)
            diet_plan = get_diet_plan(bmi)
            workout_plan = get_workout_plan(bmi)

            st.success(f"Your BMI is {bmi}")
            st.subheader("🥗 Personalized Diet Plan")
            st.info(diet_plan)
            st.subheader("💪 Recommended Workout Plan")
            st.info(workout_plan)
        else:
            st.warning("Please enter valid weight and height!")

User inputs: Takes name, age, weight, and height.

BMI Calculation: Calls calculate_bmi() to compute BMI.

Diet & Workout Plan: Fetches recommendations based on BMI.

Displays results: Uses st.success(), st.subheader(), and st.info() to show plans.

6️⃣ Water Intake Recommendation

st.subheader("📅 Water Intake Recommendation")
water_intake = round(weight * 0.033, 2)
st.write(f"You should drink approximately **{water_intake} liters** of water daily.")

Suggests daily water intake based on body weight (weight * 0.033).

📷 Screenshots

Feature

Screenshot

Main UI



BMI Result



📌 Author

Shabnam WahidFrontend Developer | Python Enthusiast
📌GitHub: Shabnam Wahid
📌 LinkedIn: Shabnamwahid

⭐ Contributions

Feel free to fork this project, create a pull request, or suggest improvements! 😊

