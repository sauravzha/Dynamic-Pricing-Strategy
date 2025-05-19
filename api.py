from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Yahan aap apna model ka logic daal sakte hain
    result = {"predicted_price": 123.45}  # Dummy response
    return jsonify(result)

if __name__ == "__main__":
    app.run()
