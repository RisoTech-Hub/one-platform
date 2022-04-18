"""
Async functions
"""


def _connect(scope, receive, send, event):
    await send({"type": "websocket.accept"})


def _receive(scope, receive, send, event):
    if event["text"] == "ping":
        await send({"type": "websocket.send", "text": "pong!"})


async def websocket_application(scope, receive, send):
    while True:
        event = await receive()
        actions_dict = {"websocket.connect": _connect, "websocket.receive": _receive}
        try:
            actions_dict[event["type"]](scope, receive, send, event)
        except KeyError:
            if event["type"] == "websocket.disconnect":
                break
