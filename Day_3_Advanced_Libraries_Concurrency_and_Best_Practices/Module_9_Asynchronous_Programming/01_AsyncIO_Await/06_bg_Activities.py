import asyncio
import aiohttp

async def consume_events():
    """Consumes events from the API endpoint."""
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:5000/random_number_stream') as response:
            async for line in response.content:
                line = line.decode('utf-8').strip()
                if line.startswith('data:'):
                    event_str = line[5:]
                    print(f"Received event: {event_str}")

async def other_tasks():
    """Simulates other background tasks."""
    print("Doing other things...")
    for i in range(5):
        print(f"Iteration {i+1}")
        await asyncio.sleep(1)
async def other_tasks_2():
    print("A new loop...")
    for i in range(5):
        print(f"Iteration from new loop {i+1}")
        await asyncio.sleep(2)
async def main():
    """Starts event consumption and other tasks concurrently."""
    await asyncio.gather(consume_events(), other_tasks(), other_tasks_2())

if __name__ == "__main__":
    asyncio.run(main())