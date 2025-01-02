# controllers/query_controller.py
class QueryController:
    def __init__(self, query_service, log_service):
        self.query_service = query_service
        self.log_service = log_service
    
    def handle_query(self, query_data, request_info):
        """
        Maneja la ejecución de queries SQL
        Args:
            query_data: dict con el query SQL
            request_info: dict con información de la petición HTTP
        """
        try:
            # Validar que venga el query
            if not query_data or 'query' not in query_data:
                return {"success": False, "message": "No se proporcionó query SQL"}, 400
            
            query = query_data['query']
            
            # Ejecutar el query
            success, result, op = self.query_service.execute_query(query)
            
            # Registrar la acción
            self.log_service.log_request(
                url=request_info.get('url'),
                endpoint=request_info.get('endpoint'),
                method=request_info.get('method'),
                user_agent_string=request_info.get('user_agent'),
                ip_address=request_info.get('ip'),
                query=query
            )
            
            if success:
                return {
                    "success": True,
                    "operation":op,
                    "data": result
                }, 200
            else:
                return {
                    "success": False,
                    "message": result,
                    "operation": op 
                }, 400
                
        except Exception as e:
            return {
                "success": False, 
                "message": f"Error ejecutando query: {str(e)}"
            }, 500