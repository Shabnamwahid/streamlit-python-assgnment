
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Healthy Diet & Workout Planner", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for Background Image on Headings
st.markdown(
    """
    <style>
    .title-heading {
        background-image: url("https://th.bing.com/th/id/R.8aff9b9238e286f6a4a6f24b9233a43f?rik=Qe2LI9DM%2fUUuSQ&pid=ImgRaw&r=0");
        background-size: cover;
        background-position: center;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sub-heading {
        background-image: url("https://www.womendailymagazine.com/wp-content/uploads/2014/09/Simple-Healthy-Diet.jpg.jpg");
        background-size: cover;
        background-position: center;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-size: 28px;
     
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Apply CSS Classes to Headings
st.markdown('<div class="title-heading">💪 Healthy Diet & Workout Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-heading">Track your health and stay fit! 🥗</div>', unsafe_allow_html=True)

# Functions for BMI, Diet & Workout Plans
def calculate_bmi(weight, height_m):
    return round(weight / (height_m ** 2), 2)

def get_diet_plan(bmi):
    if bmi < 18.5:
        return "High-protein diet with healthy fats. Include nuts, avocados, and lean meats."
    elif 18.5 <= bmi < 24.9:
        return "Balanced diet with vegetables, protein, and whole grains. Keep it steady!"
    elif 25 <= bmi < 29.9:
        return "Low-carb diet with lean proteins. Avoid processed foods. Increase activity."
    else:
        return "Strict diet with more vegetables, lean protein, and fiber. Avoid sugar & junk food."

def get_workout_plan(bmi):
    if bmi < 18.5:
        return "Light strength training and yoga to build muscle."
    elif 18.5 <= bmi < 24.9:
        return "Regular exercise: 30-minute cardio, weight training, and flexibility exercises."
    elif 25 <= bmi < 29.9:
        return "High-intensity interval training (HIIT) and strength training. Walk 10,000 steps."
    else:
        return "Low-impact cardio like swimming, cycling, and walking. Focus on gradual weight loss."

# Main App Function
def main():
    name = st.text_input("Enter Your Name")
    age = st.number_input("Enter Your Age", min_value=10, max_value=100, step=1)
    weight = st.number_input("Enter Your Weight (kg)", min_value=20, max_value=200, step=1)

    # Height Input (Feet & Inches)
    feet = st.number_input("Enter Height (Feet)", min_value=3, max_value=7, step=1)
    inches = st.number_input("Enter Height (Inches)", min_value=0, max_value=11, step=1)

    # Convert Feet & Inches to Meters
    height_m = ((feet * 12) + inches) * 0.0254  

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

            # Adding Images
            
            st.image("https://s1.1zoom.me/big0/215/Meat_products_Milk_Vegetables_Cheese_Muesli_531850_1280x838.jpg", caption="Eat Healthy!", use_container_width=True)
            st.image("https://cdn.pixabay.com/photo/2024/03/20/09/39/ai-generated-8645074_960_720.png", caption="Eat Healthy!", use_container_width=True)
        else:
            st.warning("Please enter valid weight and height!")

    st.subheader("📅 Water Intake Recommendation")
    water_intake = round(weight * 0.033, 2)
    st.write(f"You should drink approximately **{water_intake} liters** of water daily.")

if __name__ == "__main__":
    main()
