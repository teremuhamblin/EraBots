class EventBus:
    def __init__(self):
        self.history = []

    def emit(self, event_name, payload=None):
        entry = {"event": event_name, "payload": payload}
        self.history.append(entry)
