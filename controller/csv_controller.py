# controllers/csv_controller.py
from werkzeug.utils import secure_filename

class CSVController:
    def __init__(self, csv_service, log_service):
        self.csv_service = csv_service
        self.log_service = log_service
    
    def handle_upload(self, file, request_info):
        """
        Maneja la subida de un archivo CSV
        Args:
            file: El archivo subido
            request_info: dict con información de la petición HTTP
        """
        try:
            # Validar que sea un archivo
            if not file:
                return {"success": False, "message": "No se proporcionó archivo"}, 400
            
            # Validar que sea un CSV
            filename = secure_filename(file.filename)
            if not filename.endswith('.csv'):
                return {"success": False, "message": "El archivo debe ser un CSV"}, 400
            
            # Procesar el CSV
            result = self.csv_service.upload_csv(file, filename)
            
            # Registrar la acción
            self.log_service.log_request(
                url=request_info.get('url'),
                endpoint=request_info.get('endpoint'),
                method=request_info.get('method'),
                user_agent_string=request_info.get('user_agent'),
                ip_address=request_info.get('ip'),
                query=f"Upload CSV: {filename}"
            )
            
            if result['success']:
                return result, 200
            else:
                return result, 400
                
        except Exception as e:
            return {"success": False, "message": str(e)}, 500
    
    def handle_download(self, request_info):
        """
        Maneja la descarga del CSV actual
        """
        try:
            success, data = self.csv_service.download_csv()
            
            # Registrar la acción
            self.log_service.log_request(
                url=request_info.get('url'),
                endpoint=request_info.get('endpoint'),
                method=request_info.get('method'),
                user_agent_string=request_info.get('user_agent'),
                ip_address=request_info.get('ip'),
                query="Download CSV"
            )
            
            if success:
                return {"success": True, "data": data}, 200
            else:
                return {"success": False, "message": data}, 400
                
        except Exception as e:
            return {"success": False, "message": str(e)}, 500