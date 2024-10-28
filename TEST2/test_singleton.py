from corporate_data import CorporateData
from corporate_log import CorporateLog
import logging

logging.basicConfig(level=logging.DEBUG)


data_instance_1 = CorporateData()
data_instance_2 = CorporateData()
assert data_instance_1 is data_instance_2  

log_instance_1 = CorporateLog()
log_instance_2 = CorporateLog()
assert log_instance_1 is log_instance_2  

data = data_instance_1.getData(session_uuid="1234", cpu_uuid="abcd", sede_id="1")
logging.debug(f"Datos obtenidos: {data}")

data = data_instance_1.getData(session_uuid="1234", cpu_uuid="abcd", sede_id="invalid_id")
logging.debug(f"Error esperado: {data}")