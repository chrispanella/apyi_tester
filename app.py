from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from local API"})

@app.route("/process", methods=["GET"])
def process():
    contact_id_param = request.args.get("contactId")
    
    if not contact_id_param:
        received_params = dict(request.args)
        logging.error(f"Error: contactId parameter is required. Received query params: {received_params}")
        return jsonify({
            "error": "contactId parameter is required",
            "received": received_params
        }), 400
    
    # Parse comma-separated contact IDs
    contact_ids = [id.strip() for id in contact_id_param.split(",") if id.strip()]
    
    if not contact_ids:
        logging.error(f"Error: No valid contact IDs provided. Received contactId: '{contact_id_param}'")
        return jsonify({
            "error": "No valid contact IDs provided",
            "received": {
                "contactId": contact_id_param
            }
        }), 400
    
    # Process the contact IDs (you can add your processing logic here)
    result = f"Processed {len(contact_ids)} contact IDs: {contact_ids}"
    
    return jsonify({
        "result": result,
        "contact_ids": contact_ids,
        "count": len(contact_ids)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)