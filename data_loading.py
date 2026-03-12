import websocket
import json

def on_open(ws):
    print("### Connection opened ###")

def on_message(ws, message):
    data = json.loads(message)
    print("Raw message:", data)  # print full message to see current structure
    # Extract price and quantity from the trade event
    price = data.get('p', 'N/A')
    quantity = data.get('q', 'N/A')
    print(f"BTC Price: {price}, Qty: {quantity}")

def on_error(ws, error):
    print("### Error ###", error)

def on_close(ws, close_status_code, close_msg):
    print(f"### Closed ### code={close_status_code} msg={close_msg}")

if __name__ == "__main__":
    socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"
    ws = websocket.WebSocketApp(socket,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
