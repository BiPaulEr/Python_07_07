import asyncio
import random

async def fetch_weather(city):
    await asyncio.sleep(1)  # Simulez un délai de réseau
    temperature = random.randint(15, 25)  # Générez une température aléatoire
    print(f"Température pour {city} : {temperature}°C")
    return {"ville": city, "température": temperature}

async def main():
    citys = ["City1", "City2", "City3"]
    tasks = [fetch_weather(city) for city in citys]
    result = await asyncio.gather(*tasks)
    print(result)
    moyenne = sum(map(lambda x : x["température"],  result)) / len(result)
    moyenne2 = sum(x["température"] for x in result) / len(result)
    print(f"Moyenne des températures {moyenne}, {moyenne2}")
asyncio.run(main())