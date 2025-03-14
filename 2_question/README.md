# AI-Powered Solidity Contract Generator  

This project is a **Streamlit-based AI contract generator** that generates Solidity smart contracts based on user-provided descriptions.

## 🚀 Features  
- Accepts **contract descriptions** from users.  
- Matches descriptions with predefined **contract templates** stored in a JSON file.  
- Displays the best-matching **Solidity contract**.  

## 📁 Project Structure  
Internship_Assignment/  
│── data/  
│   ├── contract_prompts.json  # JSON file with contract prompts & outputs  
│── 2.py  # Main Streamlit app  
│── requirements.txt  # Dependencies  
│── README.md  # Project documentation  
│── .gitignore  # Files to exclude from Git tracking  
## 📷 Screenshots  
### **Generated Solidity Contract**
<img src="https://github.com/user-attachments/assets/b04303ee-5f79-4f01-ab20-a6ddbeef2a54" width="600">

### **User Input Screen**
<img src="https://github.com/user-attachments/assets/9ae79cc0-1825-4a54-962d-177c428d0a30" width="600">

## Installation and Run Locally  
```bash
git clone https://github.com/manojkumar063/Internship_Assignment.git  
cd Internship_Assignment  

## Install Dependencies
pip install -r requirements.txt
## Run the Streamlit App
streamlit run app.py
## 📂 Data Format (contract_prompts.json)
The JSON file should follow this format:
[
    {
        "prompt": "ERC20 token contract",
        "output": "pragma solidity ^0.8.0; contract ERC20Token { /* Solidity code */ }"
    }
]
## 🤖 How It Works
User enters a contract description in the text input field.
Script searches for a matching contract in contract_prompts.json.
Displays the best match in Solidity format


