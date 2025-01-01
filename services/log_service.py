# services/log_service.py
from datetime import datetime
from user_agents import parse  
from models.request_log_model import RequestLogTable
class LogService:
    def __init__(self, log_model):
        self.log_model = log_model
        
    def log_request(self, url, endpoint, method, user_agent_string, ip_address, query=None):
        """
        Registra una nueva petición al API con información detallada del User-Agent
        """
        try:
            # Parsear el User-Agent para obtener información detallada
            user_agent = parse(user_agent_string)
            
            log = RequestLogTable(  # Cambiado a RequestLogTable
                url=url,
                endpoint=endpoint,
                method=method,
                browser=user_agent.browser.family,
                browser_version=user_agent.browser.version_string,
                os=user_agent.os.family,
                os_version=user_agent.os.version_string,
                device_brand=user_agent.device.brand,
                ip_address=ip_address,
                query=query,
                timestamp=datetime.now()
            )
            
            self.log_model.save(log)
            return True, "Log registrado exitosamente"
            
        except Exception as e:
            return False, f"Error registrando log: {str(e)}"
        
    def get_logs(self, limit=None):
        try:
            logs = self.log_model.get_all(limit)
            return True, [log.to_dict() for log in logs]
        except Exception as e:
            return False, f"Error obteniendo logs: {str(e)}"