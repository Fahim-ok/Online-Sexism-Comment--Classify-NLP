from flask import Flask, request, jsonify, render_template
import numpy as np
from model import load_model, preprocess_text

app = Flask(__name__)

# Load the model and tokenizer
model, tokenizer = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    
    # Preprocess the text
    processed_text = preprocess_text(text, tokenizer)
    
    # Make prediction
    prediction = model.predict(processed_text)
    predicted_label = np.argmax(prediction, axis=1)[0]
    label_map = {0: 'Not Sexist', 1: 'Sexist'}
    result = label_map[predicted_label]
    
    return jsonify({'prediction': result})

if __name__ == "__main__":
    app.run(debug=True)
