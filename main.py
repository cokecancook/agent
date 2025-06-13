from hotel_bot import create_hotel_agent, AgentState, format_message_for_gemma
from hotel_bot.lm_studio import LMStudioClient

def main():
    # Initialize the agent
    agent = create_hotel_agent()
    
    # Initialize LM Studio client
    lm_client = LMStudioClient()
    
    # Initialize the state
    initial_state = {
        "messages": [
            {"role": "system", "content": """You are a hotel reception chatbot. Your role is to:
1. Greet guests professionally
2. Ask if they want to check room availability or make a reservation
3. Only provide information about rooms and prices when specifically asked
4. Never make assumptions about the guest's needs
5. Don't ask for the guest's name or any personal information
6. Try to close the reservation as soon as possible

Start by greeting the guest and asking if they would like to check availability or make a reservation."""}
        ],
        "current_availability": {},
        "reservation_status": {}
    }
    
    # Example conversation loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
            
        # Update state with user message
        initial_state["messages"].append({"role": "user", "content": user_input})
        
        # Run the agent
        result = agent.invoke(initial_state)
        
        # Format the state for Gemma
        formatted_prompt = format_message_for_gemma(result)
        
        # Get response from LM Studio using the formatted prompt
        response = lm_client.generate_response([{"role": "user", "content": formatted_prompt}])
        if response is None:
            response = "I apologize, but I'm having trouble connecting to the model. Please try again later."
        
        # Update the state with the response
        initial_state["messages"].append({"role": "assistant", "content": response})
        print(f"\nAssistant: {response}")

if __name__ == "__main__":
    main() 