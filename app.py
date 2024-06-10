import streamlit as st
from linkedlist import LinkedList
from data import cuisine_types, restaurant_info
from welcome import print_welcome

# Convert print_welcome to a Streamlit function
def streamlit_welcome():
    st.markdown("""
        <div style="text-align:center;">
            <h2>Welcome to SoHo Restaurants!</h2>
        </div>
    """, unsafe_allow_html=True)

# Insert food types into LinkedList
def insert_food_types():
    food_type_list = LinkedList()
    for food_type in cuisine_types:
        food_type_list.insert_beginning(food_type)
    return food_type_list

# Insert restaurant data into LinkedList of LinkedLists
def insert_restaurant_data():
    restaurant_data_list = LinkedList()
    for food_type in cuisine_types:
        restaurant_sublist = LinkedList()
        for restaurant in restaurant_info:
            if restaurant[0] == food_type:
                restaurant_sublist.insert_beginning(restaurant)
        restaurant_data_list.insert_beginning(restaurant_sublist)
    return restaurant_data_list

# Initialize data
my_food_list = insert_food_types()
my_restaurant_list = insert_restaurant_data()

# Streamlit app layout
st.set_page_config(page_title="Restaurant Recommender", page_icon="🍴", layout="wide")
st.title("🍴 Restaurant Recommender")
streamlit_welcome()

# Sidebar for filters
st.sidebar.header("Filter your search")
selected_food_type = st.sidebar.selectbox("Select a cuisine type:", cuisine_types)
min_rating = st.sidebar.slider("Minimum rating", 1, 5, 1)
max_price = st.sidebar.slider("Maximum price", 1, 5, 5)

# Display restaurants for the selected food type
st.subheader(f"Restaurants offering {selected_food_type} cuisine with rating >= {min_rating} and price <= {max_price}:")
for i in range(len(restaurant_info)):
    if (restaurant_info[i][0] == selected_food_type and
        int(restaurant_info[i][2]) >= min_rating and
        int(restaurant_info[i][3]) <= max_price):
        st.markdown(f"- **{restaurant_info[i][1]}** (Rating: {restaurant_info[i][2]}, Price: {restaurant_info[i][3]})\n  Address: {restaurant_info[i][4]}")

# To run this app, save it as app.py and run `streamlit run app.py` in your terminal
