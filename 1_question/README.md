## Screenshots
1️⃣ Fraud Alert
![Screenshot 2025-03-11 210056](https://github.com/user-attachments/assets/e060d87b-5644-4a15-b922-d6d78ba7f898)
2️⃣ Streamlit UI
![Screenshot 2025-03-11 205901](https://github.com/user-attachments/assets/3911392a-d76e-4c78-a6e0-94be32ca7b9a)

## Blockchain Fraud Detection System
This project is a fraud detection system for blockchain transactions. It uses a Random Forest model trained on synthetic transaction data to classify whether a transaction is fraudulent or legitimate. The system includes:

A Flask API for fraud detection.
A Streamlit UI for an interactive frontend.
## Project Structure
Internship_Assignment/
│── 1_question/
│   │── 1.py                # Generates synthetic data & trains model  
│   │── app.py              # Streamlit UI for fraud detection  
│   │── fraud_model.pkl     # Saved trained model  
│   │── synthetic_transactions.csv  # Generated dataset  
## Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/Internship_Assignment.git
cd Internship_Assignment/1_question
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Flask API
python 1.py
4️⃣ Run Streamlit App
python -m streamlit run app.py
## Usage
Enter transaction details in the Streamlit UI.
Click "Detect Fraud" to classify the transaction.
The system will alert if fraud is detected.

