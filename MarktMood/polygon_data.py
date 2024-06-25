import requests

def fetch_stock_data(symbol, date, api_key):
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{date}/{date}?apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return the JSON response as a dictionary
    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")
        return None

# Example usage
api_key = '4C2N9KdZsaC6B7PQkh8vTpZ1Bc1IiPjv'
stock_data = fetch_stock_data("AAPL", "2023-01-09", api_key)

if stock_data:
    print("Stock Data:", stock_data)
else:
    print("No data received.")
