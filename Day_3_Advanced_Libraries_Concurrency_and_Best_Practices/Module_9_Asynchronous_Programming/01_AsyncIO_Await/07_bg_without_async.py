import requests
import time

def consume_events():
    """Consumes events from the API endpoint without asyncio."""
    response = requests.get('http://127.0.0.1:5000/random_number_stream', stream=True)
#    for line in response.iter_lines():
    for line in response.iter_lines():
        line = line.decode('utf-8').strip()
        if line.startswith('data:'):
            event_str = line[5:]
            print(f"Received event: {event_str}")

def other_tasks():
    """Simulates other background tasks."""
    print("Doing other things...")
    for i in range(5):
        print(f"Iteration {i+1}")
        time.sleep(1)

def other_tasks_2():
    """Simulates another set of background tasks."""
    print("A new loop...")
    for i in range(5):
        print(f"Iteration from new loop {i+1}")
        time.sleep(2)

if __name__ == "__main__":
    consume_events()  # This will block until it completes
    other_tasks()     # This will run only after consume_events() finishes
    other_tasks_2()   # This will run only after other_tasks() finishes