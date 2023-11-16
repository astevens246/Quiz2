from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Define the base URL for SWAPI
SWAPI_BASE_URL = "https://swapi.py4e.com/api/"

@app.route('/character', methods=['GET', 'POST'])
def character():
    # Check if the request method is POST
    if request.method == 'POST':
        # Extract the character ID from the form data
        character_id = request.form['character_id']
        
        # Retrieve character data from the SWAPI using the character ID
        character_data = get_character_data(character_id)
        
        # Check if character data is available
        if character_data:
            # Render the character.html template with character data
            return render_template('character.html', character_data=character_data)
        else:
            # If character data is not found, display an error message
            error_message = f"Character with ID {character_id} not found."
            return render_template('character.html', error_message=error_message)
    
    # If the request method is GET, render the character_form.html template
    return render_template('character_form.html')

def get_character_data(character_id):
    try:
        # Make a GET request to the SWAPI to retrieve character data
        response = requests.get(f"{SWAPI_BASE_URL}/people/{character_id}")
        
        # Check if the request was successful (status code 2xx)
        response.raise_for_status()  # Raises an error for bad requests
        
        # Parse the JSON response containing character data
        character_data = response.json()
        return character_data
    except requests.exceptions.HTTPError:
        # Handle HTTP errors, return None if character not found
        return None

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
