AI-Powered Solidity Contract Generator
This project is a Streamlit-based AI contract generator that generates Solidity smart contracts based on user-provided descriptions.

🚀 Features
Accepts contract descriptions from users.
Matches descriptions with predefined contract templates stored in a JSON file.
Displays the best-matching Solidity contract.
📁 Project Structure
Internship_Assignment/ │── data/ │ ├── contract_prompts.json # JSON file with contract prompts & outputs │── 2.py # Main Streamlit app │── requirements.txt # Dependencies │── README.md # Project documentation │── .gitignore # Files to exclude from Git tracking ##clone repository git clone https://github.com/manojkumar063/Internship_Assignment.git cd Internship_Assignment ##Install Dependencies pip install -r requirements.txt ##Run the Streamlit App python -m streamlit run 2.py 🤖How It Works User enters a contract description in the text input field. Script searches for a matching contract in contract_prompts.json. Displays the best match in Solidity format
