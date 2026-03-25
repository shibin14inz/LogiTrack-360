import asyncio
import json
import random
import websockets

# Simulation Constants
TOTAL_TRUCKS = 500
SERVER_URL = "ws://localhost:8000/ws/truck"
PING_INTERVAL = 5  # Seconds between updates

async def simulate_truck(truck_id):
    url = f"{SERVER_URL}/{truck_id}"
    try:
        async with websockets.connect(url) as websocket:
            print(f"Truck {truck_id}: Connected")
            
            # Initial starting point (near a warehouse)
            lat, lng = 12.9716, 77.5946 
            
            while True:
                # 1. Simulate movement (small random jitter)
                lat += random.uniform(-0.001, 0.001)
                lng += random.uniform(-0.001, 0.001)
                
                # 2. Simulate engine data
                engine_temp = random.uniform(70, 110) # Potential alert trigger
                fuel = random.uniform(20, 100)
                
                payload = {
                    "latitude": lat,
                    "longitude": lng,
                    "engine_temp": engine_temp,
                    "fuel_level": fuel,
                    "speed": random.uniform(30, 80)
                }
                
                # 3. Send to FastAPI
                await websocket.send(json.dumps(payload))
                await asyncio.sleep(PING_INTERVAL)
                
    except Exception as e:
        print(f"Truck {truck_id}: Connection failed - {e}")

async def run_fleet():
    tasks = []
    for i in range(1, TOTAL_TRUCKS + 1):
        tasks.append(simulate_truck(i))
    
    # Run all 500 trucks concurrently
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(run_fleet())
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")