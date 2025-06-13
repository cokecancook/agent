import json
from .state import AgentState, hotel_availability

def format_message_for_gemma(state: AgentState) -> str:
    """Format the current state into a prompt for Gemma."""
    messages = state["messages"]
    availability = state.get("current_availability", {})
    reservation = state.get("reservation_status", {})
    
    context = f"""You are a helpful hotel reception chatbot. Current hotel availability:
    Standard rooms: {hotel_availability['standard']['available']} available at ${hotel_availability['standard']['price']}
    Deluxe rooms: {hotel_availability['deluxe']['available']} available at ${hotel_availability['deluxe']['price']}
    Suites: {hotel_availability['suite']['available']} available at ${hotel_availability['suite']['price']}
    
    Current conversation context:
    """
    
    for msg in messages:
        context += f"{msg['role']}: {msg['content']}\n"
    
    if availability:
        context += f"\nCurrent availability check: {json.dumps(availability)}\n"
    if reservation:
        context += f"\nReservation status: {json.dumps(reservation)}\n"
    
    return context