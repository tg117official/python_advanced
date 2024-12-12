import random
import time
from flask import Flask, Response

app = Flask(__name__)

def event_stream():
    """Generates a stream of random number events."""
    while True:
        # Generate a random integer between 1 and 100
        random_number = random.randint(1, 100)

        # Create a dictionary to represent the event
        event = {
            'eventType': 'randomNumberGenerated',
            'data': {
                'randomNumber': random_number
            }
        }
        # Yield the event as a JSON response with Server-Sent Events formatting
        yield f"data: {event}\n\n"
        time.sleep(5)  # Wait for 5 seconds

@app.route('/random_number_stream')
def random_number_stream():
    """Returns a stream of random number events."""
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True)