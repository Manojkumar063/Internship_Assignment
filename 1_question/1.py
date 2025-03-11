import pandas as pd
import random
import uuid
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import Flask, request, jsonify
import joblib
import os

# Generate synthetic dataset
data = []
for _ in range(1000):
    tx_id = str(uuid.uuid4())
    sender = "0x" + ''.join(random.choices('abcdef0123456789', k=40))
    receiver = "0x" + ''.join(random.choices('abcdef0123456789', k=40))
    amount = round(random.uniform(0.001, 100), 4)
    gas_fee = round(random.uniform(0.0001, 0.1), 5)
    tx_count = random.randint(1, 200)
    is_fraud = 1 if (amount > 80 or (gas_fee > 0.08 and tx_count > 150)) else 0
    data.append([tx_id, sender, receiver, amount, gas_fee, tx_count, is_fraud])

df = pd.DataFrame(data, columns=['transaction_id', 'sender_address', 'receiver_address', 'amount', 'gas_fee', 'transaction_count', 'is_fraud'])

# Save dataset
df.to_csv('synthetic_transactions.csv', index=False)

# Prepare data for ML
X = df[['amount', 'gas_fee', 'transaction_count']]
y = df['is_fraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, 'fraud_model.pkl')

# Flask API
app = Flask(__name__)

@app.route('/detect_fraud', methods=['POST'])
def detect_fraud():
    data = request.get_json()
    features = [[data['amount'], data['gas_fee'], data['transaction_count']]]
    model = joblib.load('fraud_model.pkl')
    prediction = model.predict(features)[0]
    return jsonify({'is_fraud': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
