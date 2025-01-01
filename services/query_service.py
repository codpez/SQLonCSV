# services/query_service.py
from sqlalchemy import text
from sql.interpreter import SQLInterpreter  # Tu intérprete personalizado

class QueryService:
    def __init__(self, csv_model):
        """
        Inicializa el servicio con una referencia al modelo CSV
        y crea una instancia del intérprete SQL
        """
        self.csv_model = csv_model
        self.interpreter = SQLInterpreter()
        
    def execute_query(self, query):
        """
        Ejecuta un query SQL después de validarlo con el intérprete
        """
        try:
            # Usar tu parser para validar
            parsed = self.interpreter.interpret(query)
            command_type = parsed[0] if isinstance(parsed, tuple) else None
            
            if command_type is None:
                return False, "Error en el parsing del query"
            

            # Ejecutar en la base de datos
            engine = self.csv_model.get_engine()
            with engine.connect() as conn:
                result = conn.execute(text(query))
                
                if command_type.upper() == "SELECT":
                    columns = result.keys()
                    result_list = [dict(zip(columns, row)) for row in result]
                    return True, result_list
                else:
                    conn.commit()
                    return True, f"Operación exitosa. Filas afectadas: {result.rowcount}"
                    
        except Exception as e:
            return False, str(e)