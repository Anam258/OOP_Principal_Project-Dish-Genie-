# app.py
import streamlit as st
from dish_data import get_dishes_by_weather
from dish import Dish

class DishGenieApp:
    """
    🔹 OOP Principle: Encapsulation
    This class handles all logic related to dish suggestion based on weather.
    """
    def __init__(self):
        self.weather = None
        self.dish_index = 0
        self.liked = False
        self.dishes_by_weather = get_dishes_by_weather()  # 🍽️ Data abstraction

    def suggest_dish(self):
        """🔹 OOP Principle: Abstraction — Suggest next dish without exposing logic"""
        if self.weather:
            dish_list = self.dishes_by_weather[self.weather]
            if self.dish_index < len(dish_list):
                return dish_list[self.dish_index]
        return None

    def display_dish(self, dish):
        """🔹 OOP Principle: Abstraction — Display dish info in clean way"""
        st.subheader(f"✨ {dish.get_name()}")
        st.write(dish.get_description())
        if dish.get_image():
            st.image(dish.get_image(), use_container_width=True)

    def load_custom_css(self):
        """✅ Load external CSS for background styling"""
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def run(self):
        """🔹 Main method to run the Streamlit UI"""
        
        # 🔹 OOP Principle: Encapsulation of UI logic
        st.set_page_config(page_title="Dish Genie 🍽️", page_icon="✨")  # Move this to the top as per Streamlit's requirement
        self.load_custom_css()  # ✅ Load background style after page config
        st.title("🍲 Dish Genie — Your Food Advisor")

        # ✅ Initialize session state properly
        if 'weather' not in st.session_state:
            st.session_state.weather = None
        if 'dish_index' not in st.session_state:
            st.session_state.dish_index = 0
        if 'liked' not in st.session_state:
            st.session_state.liked = False

        # 🔸 UI: Weather selection
        st.markdown("### How’s the weather today?")
        weather = st.selectbox("Select Weather", options=["Sunny", "Rainy", "Cold"])

        if st.button("🎲 Suggest Me a Dish"):
            st.session_state.weather = weather
            st.session_state.dish_index = 0
            st.session_state.liked = False

        # 🔸 Display dish suggestion
        if st.session_state.weather:
            self.weather = st.session_state.weather
            self.dish_index = st.session_state.dish_index
            dish = self.suggest_dish()

            if dish:
                self.display_dish(dish)

                # 🔸 Like / Next Buttons
                col1, col2 = st.columns(2)
                with col1:
                    like_clicked = st.button("🎉 I like it!", key="like")
                with col2:
                    another_clicked = st.button("🔁 Suggest Another", key="another")
                    if like_clicked:
                        st.balloons()
                        st.success("Great choice! Enjoy your meal! 🍽️😋")
                    if another_clicked:
                        st.session_state.dish_index += 1
            else:
                st.warning("No more dishes for this weather. Restart to try another!")

# 🔹 Run the app
if __name__ == "__main__":
    app = DishGenieApp()
    app.run()
