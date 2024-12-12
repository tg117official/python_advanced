import asyncio
import aiohttp

async def consume_events():
  """Consumes events from the API endpoint."""
  async with aiohttp.ClientSession() as session:
    async with session.get('http://127.0.0.1:5000/random_number_stream') as response:
      async for line in response.content:
        line = line.decode('utf-8').strip()
        if line.startswith('data:'):
          event_str = line[5:]  # Remove the 'data: ' prefix
          # Process the event data (e.g., print it or store it)
          print(f"Received event: {event_str}")

async def main():
  """Starts the event consumption."""
  await consume_events()

if __name__ == "__main__":
  asyncio.run(main())