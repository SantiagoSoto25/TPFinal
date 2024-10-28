class CorporateData:
    _instance = None
    _data = {
        "1": {
            "id": "1",
            "domicilio": "Calle Falsa 123",
            "localidad": "Springfield",
            "cp": "12345",
            "provincia": "Illinois",
            "CUIT": "20-12345678-9",
            "idSeq": 1000
        }
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CorporateData, cls).__new__(cls)
        return cls._instance

    def getData(self, session_uuid, cpu_uuid, sede_id):
        return self._data.get(sede_id, {"error": "No data found"})

    def getCUIT(self, session_uuid, cpu_uuid, sede_id):
        data = self.getData(session_uuid, cpu_uuid, sede_id)
        return {"CUIT": data.get("CUIT", "No CUIT found")} if "error" not in data else data

    def getSeqID(self, session_uuid, cpu_uuid):
        sequence_data = self._data.get("1", {})
        if "idSeq" in sequence_data:
            sequence_data["idSeq"] += 1
            return {"idSeq": sequence_data["idSeq"]}
        return {"error": "Sequence ID not found"}

    def listCorporateData(self, sede_id):
        return list(self._data.values())
