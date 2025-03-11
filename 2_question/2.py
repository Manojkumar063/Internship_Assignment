import json
import os
import streamlit as st

# Ensure the file path is correct
json_file_path = os.path.join("data", "contract_prompts.json")

# Load dataset
try:
    with open(json_file_path, "r") as file:
        contracts = json.load(file)
except FileNotFoundError:
    st.error(f"File {json_file_path} not found! Ensure the JSON file exists.")
    st.stop()

# Streamlit UI
st.title("AI-Powered Solidity Contract Generator")

prompt = st.text_input("Enter your contract description:")

if st.button("Generate Contract"):
    prompt_lower = prompt.lower()

    # Find the best match
    best_match = None
    for entry in contracts:
        if all(word in entry["prompt"].lower() for word in prompt_lower.split()):
            best_match = entry["output"]
            break

    if best_match:
        st.subheader("Generated Solidity Contract:")
        st.code(best_match, language="solidity")
    else:
        st.error("No matching contract found!")
