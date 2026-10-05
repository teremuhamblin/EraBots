class SessionManager:
    def __init__(self):
        self.sessions = {}

    def start_session(self, user_id):
        session_id = f"session-{user_id}"
        self.sessions[session_id] = {
            "messages": [],
            "context": {}
        }
        return session_id

    def add_message(self, session_id, message):
        self.sessions[session_id]["messages"].append(message)

    def get_context(self, session_id):
        return self.sessions[session_id]["context"]
