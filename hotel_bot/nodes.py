from datetime import datetime
from .state import AgentState, hotel_availability

def check_availability(state: AgentState) -> AgentState:
    """Check room availability based on the conversation."""
    messages = state["messages"]
    last_message = messages[-1]["content"].lower()
    
    # Simple keyword matching for room types
    room_type = None
    if "standard" in last_message:
        room_type = "standard"
    elif "deluxe" in last_message:
        room_type = "deluxe"
    elif "suite" in last_message:
        room_type = "suite"
    
    if room_type:
        availability = hotel_availability[room_type]
        state["current_availability"] = {
            "room_type": room_type,
            "available": availability["available"],
            "price": availability["price"]
        }
    else:
        state["current_availability"] = {"error": "No specific room type mentioned"}
    
    return state

def make_reservation(state: AgentState) -> AgentState:
    """Attempt to make a reservation if requested."""
    messages = state["messages"]
    last_message = messages[-1]["content"].lower()
    
    if "book" in last_message or "reserve" in last_message:
        availability = state.get("current_availability", {})
        if "room_type" in availability and availability["available"] > 0:
            # In a real system, this would update a database
            hotel_availability[availability["room_type"]]["available"] -= 1
            state["reservation_status"] = {
                "success": True,
                "room_type": availability["room_type"],
                "price": availability["price"],
                "confirmation_number": f"CONF-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            }
        else:
            state["reservation_status"] = {
                "success": False,
                "error": "Room not available"
            }
    else:
        state["reservation_status"] = {"status": "No reservation requested"}
    
    return state 