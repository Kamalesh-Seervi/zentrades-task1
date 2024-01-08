from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def display_data():
    # Fetch JSON data from the API
    url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        products = data.get('products', {})

        if products:
            product_list = list(products.values())
            sorted_products = sorted(product_list, key=lambda x: int(x['popularity']), reverse=True)

            result = ""
            for product in sorted_products:
                result += f"Title: {product['title']}<br>"
                result += f"Price: {product['price']}<br>"
                result += f"Popularity: {product['popularity']}<br>"
                result += f"Subcategory: {product['subcategory']}<br>"
                result += "=" * 30 + "<br>"

            return result

if __name__ == '__main__':
    app.run(host ='127.0.0.1', port = 8080,debug=True)