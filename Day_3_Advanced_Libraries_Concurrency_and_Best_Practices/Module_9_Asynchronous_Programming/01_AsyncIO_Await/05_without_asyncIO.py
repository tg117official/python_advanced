import requests
import time

def consume_events():
  """Consumes events from the API endpoint without asyncio."""

  # Challenge 1: Blocking requests
  #   - `requests.get` blocks until the whole response is received.
  #   - This can make the program unresponsive while waiting.
  response = requests.get('http://127.0.0.1:5000/random_number_stream', stream=True)

  # Challenge 2: Manual iteration and parsing
  #   - We need to iterate over the response content manually.
  #   - We need to handle potential incomplete lines and parsing errors.
  for line in response.iter_lines():
    line = line.decode('utf-8').strip()
    if line.startswith('data:'):
      event_str = line[5:]  # Remove the 'data: ' prefix
      # Process the event data (e.g., print it or store it)
      print(f"Received event: {event_str}")

    # Challenge 3: No built-in mechanism for concurrency
    #   - Handling multiple events or tasks concurrently would require
    #     complex threading or multiprocessing techniques.

if __name__ == "__main__":
  consume_events()