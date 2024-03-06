# import libraries
import streamlit as st
from travel_agent import get_travel_suggestions

# Define the main function
def main():
    st.title('LangChain Travel Planner')
    # Add inputs for the user to enter their travel details
    origin = st.text_input('Where are you traveling from?') 
    destination = st.text_input('Which destination would you like to travel to?')
    budget = st.number_input('What is your budget for the trip?', min_value=100, max_value=10000, value=1000)  # Alterado para number_input para permitir entrada de valores exatos
    interests = st.multiselect('What kind of activities interest you?', 
                               ['Culture', 'Adventure', 'Relaxation', 'Gastronomy', 'Sports'])

    if st.button('Get Travel Suggestions'):
        # Check if the inputs are not empty
        if origin and destination and budget and interests:  
            suggestions = get_travel_suggestions(origin, destination, budget, interests)
            st.write('Suggestions:', suggestions)
        else:
            st.error("Please fill in all the fields.")

if __name__ == '__main__':
    main()