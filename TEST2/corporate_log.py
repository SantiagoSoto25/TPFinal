class CorporateLog:
    _instance = None
    _log = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CorporateLog, cls).__new__(cls)
        return cls._instance

    def post(self, session_uuid, method_name):
        log_entry = {
            'uuid': session_uuid,
            'cpu_uuid': str(uuid.getnode()),
            'method': method_name,
            'timestamp': int(time.time())
        }
        self._log.append(log_entry)
        return {"status": "log saved"}

    def list(self, cpu_uuid, session_uuid=None):
        return self._log
