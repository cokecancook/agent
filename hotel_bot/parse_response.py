import json

# Example response.content
response_content = b'{"model":"gemma:2b","created_at":"2025-06-13T15:27:40.471801089Z","response":"I am an AI chatbot and do not have feelings or the ability to experience life in the same way humans do. I am here to assist you with any questions or tasks you may have.","done":true,"done_reason":"stop","context":[968,2997,235298,559,235298,15508,235313,1645,108,2299,708,692,235336,107,235248,108,235322,2997,235298,559,235298,15508,235313,2516,108,235285,1144,671,16481,183294,578,749,780,791,14690,689,573,7374,577,3281,1913,575,573,1809,1703,17611,749,235265,590,1144,1517,577,5422,692,675,1089,3920,689,13333,692,1249,791,235265],"total_duration":6321742170,"load_duration":67777000,"prompt_eval_count":26,"prompt_eval_duration":1958760335,"eval_count":39,"eval_duration":4290078043}'

# Decode bytes to string and parse JSON
response_data = json.loads(response_content.decode('utf-8'))

# Access different parts of the response
print("Model:", response_data["model"])
print("Response:", response_data["response"])
print("Created at:", response_data["created_at"])
print("Done:", response_data["done"])
print("Done reason:", response_data["done_reason"])

# Access performance metrics
print("\nPerformance Metrics:")
print("Total duration:", response_data["total_duration"] / 1e9, "seconds")  # Convert nanoseconds to seconds
print("Load duration:", response_data["load_duration"] / 1e9, "seconds")
print("Prompt eval count:", response_data["prompt_eval_count"])
print("Prompt eval duration:", response_data["prompt_eval_duration"] / 1e9, "seconds")
print("Eval count:", response_data["eval_count"])
print("Eval duration:", response_data["eval_duration"] / 1e9, "seconds") 