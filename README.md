# AI Travel Planner

## Project Overview
The AI Travel Planner is an intelligent web application that helps users plan personalized trips based on their preferences. By entering details such as source, destination, duration, budget, and interests, the system generates a complete itinerary including recommended places, activities, and estimated travel details. The app is designed to simplify travel planning and provide users with efficient, customized suggestions.

---

## Features
- Personalized travel itinerary generation
- Input options for source, destination, duration, budget, and interests
- Reset option to clear inputs and generate new plans
- User-friendly interface built with Streamlit
- Efficient data handling using Pandas and JSON
- AI-powered recommendations using Google Generative AI (Gemini)

---

## Problem Statement
Planning a trip can often be overwhelming due to the vast amount of information available online and the numerous factors that need to be considered—such as destinations, budgets, accommodation, weather, and activities. Many travelers, especially first-time planners, struggle to create well-structured itineraries that match their preferences, time, and budget.

Traditional travel planning methods are time-consuming, confusing, and often lack personalization. This creates a need for an AI-powered travel assistant that can provide personalized, efficient, and data-driven itinerary suggestions, making trip planning simpler, faster, and more enjoyable for users.

---

## System Development Approach
- **Frontend:** Streamlit – interactive interface with input forms and reset option.  
- **Backend:** Python – handles logic and orchestrates communication between frontend and AI engine.  
- **Engine/Model:** Google Generative AI (Gemini) – generates personalized travel itineraries and recommendations.  
- **Data Handling:** Pandas and JSON – stores, organizes, and processes user preferences and generated travel plans.  

---

## Algorithm & Deployment

### Algorithm Steps:
1. User enters travel details: source, destination, duration, budget, and interests.  
2. System validates and structures the input data.  
3. User data is sent to the AI engine to generate a personalized itinerary.  
4. Generated itinerary is processed and formatted for display.  
5. Display the itinerary on the Streamlit interface with an option to reset or regenerate.  

### Deployment Steps:
1. Develop and test the app locally using Streamlit.  
2. Install required dependencies using `requirements.txt`.  
3. Integrate the AI engine into the backend.  
4. Deploy the app on Streamlit Cloud.  
5. Test all functionalities including input, generation, display, and reset option.  

---

## Result
- Generates **AI-based personalized travel itineraries** based on user input.  
- Displays a well-structured plan including destinations, activities, and travel details.  
- Supports **reset and regeneration** for multiple planning attempts.  
- Provides a seamless and interactive user experience.

---

## Conclusion
The AI Travel Planner effectively simplifies the travel planning process by generating tailored itineraries. It demonstrates the power of AI in enhancing user experience and decision-making, offering travelers a convenient and personalized way to plan trips.

---

## Future Scope
- Add **voice input** and chatbot interface for interactive planning.  
- Include **multi-language support** for global travelers.  
- Integrate **hotel and flight booking features**.  
- Implement **budget optimization and group travel planning**.  

---

## References
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Google Generative AI Documentation](https://ai.google.dev/)  
- [Pandas Documentation](https://pandas.pydata.org/docs/)  

