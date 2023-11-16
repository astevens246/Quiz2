from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Define the base URL for SWAPI
SWAPI_BASE_URL = "https://swapi.py4e.com/api/"

@app.route('/character', methods= ['GET', 'POST'])
def character():
    if request.method == 'POST':
        character_id = request.form['character_id']
        character_data = get_character_data(character_id)
        
        if character_data: 
            return render_template('character.html', character_data=character_data)
        else: 
            error_message = f"Character with ID {character_id} not found."
            return render_template('character.html', error_message=error_message)
    return render_template('character_form.html')

def get_character_data(character_id):
    try: 
        response = requests.get(f"{SWAPI_BASE_URL}/people/{character_id}")
        response.raise_for_status() #raises error for bad requests
        
        character_data = response.json()
        return character_data
    except requests.exceptions.HTTPError:
        return None
    
if __name__ == '__main__':
    app.run(debug=True)
