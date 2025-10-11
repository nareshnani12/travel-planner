import streamlit as st
from google import genai
import datetime

Client=genai.Client(api_key='AIzaSyAUJY9wFrtkdpW3vyPJ98RESc3bP2oEHsY')



st.title("Nani's planner💕")

if "strating_point" not in st.session_state:
    st.session_state.strating_point = ""
if "destinations" not in st.session_state:
    st.session_state.destinations = ""
if "starting_date" not in st.session_state:
    st.session_state.starting_date = datetime.date.today()
if "ending_date" not in st.session_state:
    st.session_state.ending_date = datetime.date.today()
if "number_of_people" not in st.session_state:
    st.session_state.number_of_people = 1
if "currency" not in st.session_state:
    st.session_state.currency = "INR"
if "budget" not in st.session_state:
    st.session_state.budget = 1000
if "trip_type" not in st.session_state:
    st.session_state.trip_type = "Adventure"
if "preferences" not in st.session_state:
    st.session_state.preferences = ""



with st.form("travel-form"):
    strating_point=st.text_input("Enter your starting point(city or landmark)",key="strating_point",placeholder="e.g.,Hyderabad,Mumbai,Visakhapatnam")
    destinations=st.text_input("Enter your destination(city or landmark) with comma separated",key="destinations",placeholder="e.g.,Goa,Thailand,kerala")
    starting_date=st.date_input("Enter your starting date",key="starting_date",min_value=datetime.date.today())
    ending_date=st.date_input("Enter your ending date",key="ending_date",min_value=st.session_state.starting_date)
    number_of_people=st.number_input("Enter number of people",min_value=1,key="number_of_people")
    currency=st.selectbox("Select your currency",options=["INR","USD","EUR","GBP","JPY","AUD","CAD"],key="currency")
    budget=st.number_input("Enter your budget",min_value=1000,key="budget")
    trip_type=st.selectbox("Select your trip type",options=["Adventure","Relaxation","Cultural","Romantic","Family"],key="trip_type")
    preferences=st.text_area("Any specific preferences or interests? (optional)",key="preferences",placeholder="e.g.,Hiking,museums,local cuisine,beaches")





    submit_button = st.form_submit_button("Get Travel plan",type="primary")
if submit_button:
    if not all([
        st.session_state.strating_point,
        st.session_state.destinations,
        st.session_state.starting_date,
        st.session_state.ending_date,
        st.session_state.currency,
        st.session_state.budget,
        st.session_state.trip_type
    ]):
        st.error("Please fill all the fields")
    else:
        with st.spinner("Generating your travel plan with pure hearts..."):
            prompt=f"""
            Create a detailed daily travel itinerary with the following information:
            starting from:{strating_point}
            Destinations to visit:{destinations}
            Trip strat from{starting_date} to {ending_date}
            Number of people:{number_of_people}
            Budget:{budget} {currency}
            Travel style:{trip_type}
            Preferences:{preferences if preferences else 'None'}

            Please provide a day-by-day itinerary including:
            1.Transportation options between locations
            2.Recommend accommodations within the budget
            3.key attractions to visit each day
            4.Estimated costs for each activity and meal
            5.Local cuisine recommendations
            6.Any practical tips for travelers

            Format the response in a clear,organised manner with sections for each day."""

            response=Client.models.generate_content(model="gemini-2.5-flash",contents=prompt)
            st.write(response.text)
            st.download_button(
                label="Download Itinerary",
                data=response.text,
                file_name="travel_itinerary.txt",
                mime="text/plain"
            )

def reset_form():
    st.session_state["strating_point"] = ""
    st.session_state["destinations"] = ""
    st.session_state["starting_date"] = datetime.date.today()
    st.session_state["ending_date"] = datetime.date.today()
    st.session_state["number_of_people"] = 1
    st.session_state["currency"] = "INR"
    st.session_state["budget"] = 1000
    st.session_state["trip_type"] = "Adventure"
    st.session_state["preferences"] = ""

st.button("Reset", on_click=reset_form)

