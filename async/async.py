import asyncio
import json
from datetime import datetime


async def task2():
    await asyncio.sleep(2)
    with open("data_1.json", "r") as file:
        data = json.load(file)
        print("Data loaded")
        names = []
        prices = []
        for i in data["movies"]:
            names.append(i["name"])
            prices.append(i["price"])

    whole_data = {"names": names, "prices": prices}
    await task1(whole_data)


async def task1(data):
    await asyncio.sleep(2)
    with open("data_2.json", "w") as file1:
        json.dump(data, file1, indent=4)


async def main():
    await asyncio.gather(task2())


if __name__ == "__main__":
    print(datetime.now().time())
    asyncio.run(main())
    print(datetime.now().time())
