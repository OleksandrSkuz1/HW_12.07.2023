import json

if __name__ == '__main__':
    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)
        print(products)

        temp_arr = []
        for item in products:
            if title[0].upper() == "F":
                temp_arr.append(item)

