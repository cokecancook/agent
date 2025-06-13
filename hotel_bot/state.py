from typing import Dict, TypedDict, Annotated, Sequence

class AgentState(TypedDict):
    messages: Annotated[Sequence[Dict], "The messages in the conversation"]
    current_availability: Annotated[Dict, "Current hotel availability"]
    reservation_status: Annotated[Dict, "Status of any reservation attempt"]

# Initialize hotel availability (in a real system, this would be a database)
hotel_availability = {
    "standard": {"available": 5, "price": 100},
    "deluxe": {"available": 3, "price": 150},
    "suite": {"available": 2, "price": 250}
} 