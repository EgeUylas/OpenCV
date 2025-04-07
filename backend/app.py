from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
import os
import io
import uuid
import base64

app = Flask(__name__)
CORS(app)

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    
    # Generate a unique filename
    filename = str(uuid.uuid4()) + os.path.splitext(image_file.filename)[1]
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    # Save the image
    image_file.save(filepath)
    
    return jsonify({
        'message': 'Image uploaded successfully',
        'filename': filename
    })

@app.route('/process', methods=['POST'])
def process_image():
    data = request.json
    
    if not data or 'filename' not in data:
        return jsonify({'error': 'No filename provided'}), 400
    
    filename = data['filename']
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    if not os.path.exists(filepath):
        return jsonify({'error': 'Image not found'}), 404
    
    try:
        # Open the image
        img = Image.open(filepath)
        
        # Process the image based on the parameters
        if 'resize' in data and data['resize']:
            width = int(data['width'])
            height = int(data['height'])
            img = img.resize((width, height), Image.LANCZOS)
        
        if 'rotate' in data and data['rotate']:
            angle = float(data['angle'])
            img = img.rotate(angle, expand=True)
        
        if 'flip' in data:
            if data['flip'] == 'horizontal':
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif data['flip'] == 'vertical':
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
        
        if 'crop' in data and data['crop']:
            left = int(data['left'])
            top = int(data['top'])
            right = int(data['right'])
            bottom = int(data['bottom'])
            img = img.crop((left, top, right, bottom))
        
        # Save the processed image
        processed_filename = 'processed_' + filename
        processed_filepath = os.path.join(UPLOAD_FOLDER, processed_filename)
        img.save(processed_filepath)
        
        # Convert the processed image to base64 for sending back to the client
        buffered = io.BytesIO()
        img.save(buffered, format=img.format or 'JPEG')
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({
            'message': 'Image processed successfully',
            'processed_image': img_str,
            'processed_filename': processed_filename
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        return send_file(filepath)
    else:
        return jsonify({'error': 'Image not found'}), 404

if __name__ == '__main__':
    app.run(debug=True) 