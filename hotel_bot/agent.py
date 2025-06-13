from langgraph.graph import StateGraph
from .state import AgentState
from .nodes import check_availability, make_reservation

def should_continue(state: AgentState) -> str:
    """Determine the next node based on the state."""
    messages = state["messages"]
    last_message = messages[-1]["content"].lower()
    
    # Get the current status
    reservation_status = state.get("reservation_status", {})
    current_status = reservation_status.get("status", "")
    
    # Handle error states
    if current_status == "error":
        return "end"
    
    # Handle completed states
    if current_status == "reserved":
        return "end"
    
    # Handle checked availability
    if current_status == "checked":
        # If they want to make a reservation, go to make_reservation
        booking_keywords = ["book", "reserve", "reservation", "booking", "make a reservation"]
        if any(keyword in last_message for keyword in booking_keywords):
            return "make_reservation"
        # Otherwise end the conversation
        return "end"
    
    # Handle pending reservations
    if current_status == "pending":
        # Check for confirmation
        confirmation_keywords = ["yes", "confirm", "proceed", "book it", "reserve it", "go ahead"]
        if any(keyword in last_message for keyword in confirmation_keywords):
            return "make_reservation"
        # If they say no or want to check availability again
        if "no" in last_message or "check" in last_message:
            return "check_availability"
        # Otherwise stay in make_reservation
        return "make_reservation"
    
    # For new conversations, start with availability check
    return "check_availability"

def end(state: AgentState) -> AgentState:
    """End node that returns the final state."""
    return state

def create_hotel_agent():
    """Create and configure the hotel agent workflow."""
    # Create the graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("check_availability", check_availability)
    workflow.add_node("make_reservation", make_reservation)
    workflow.add_node("end", end)
    
    # Define the edges with conditional routing
    workflow.add_conditional_edges(
        "check_availability",
        should_continue,
        {
            "make_reservation": "make_reservation",
            "end": "end"
        }
    )
    
    workflow.add_conditional_edges(
        "make_reservation",
        should_continue,
        {
            "make_reservation": "make_reservation",
            "end": "end"
        }
    )
    
    # Set the entry point
    workflow.set_entry_point("check_availability")
    
    # Compile the graph
    return workflow.compile() 