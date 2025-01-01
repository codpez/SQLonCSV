# services/csv_service.py
import pandas as pd
import os
from models.csv_model import CSVModel


class CSVService:
    def __init__(self,csv_model):
        self.csv_model = csv_model
        self.csv_model.initialize_db()
        
    def upload_csv(self, file, filename):
        """
        Procesa la subida de un archivo CSV

        Retorna:
            dict: Resultado de la operación con metadata
        """
        response = {
            "success": False,
            "message": "",
            "preview": None,
            "metadata": None
        }
        
        try:
            # Lee y valida el CSV
            df = pd.read_csv(file)
            
            # Validaciones básicas
            if df.empty:
                response["message"] = "El CSV está vacío"
                return response
                
            
            # Almacena en el modelo
            self.csv_model.store_dataframe(df, filename)
            print(self.csv_model.table_name)
            # Prepara respuesta
            response.update({
                "success": True,
                "message": "CSV cargado exitosamente",
                "preview": df.head(3).to_dict('records'),
                "metadata": self.csv_model.get_table_info()
            })
            
        except pd.errors.EmptyDataError:
            response["message"] = "El archivo está vacío o mal formateado"
        except pd.errors.ParserError:
            response["message"] = "El archivo no tiene un formato CSV válido"
        except Exception as e:
            response["message"] = f"Error procesando CSV: {str(e)}"
            
        return response
        
    def download_csv(self):
        """
        Genera un CSV con los datos actuales de la tabla
        Returns:
            tuple: (éxito, datos o mensaje de error)
        """
        try:
            engine = self.csv_model.get_engine()
            table_name = self.csv_model.table_name
            
            if not engine or not table_name:
                return False, "No hay datos cargados para descargar"
            
            # Lee los datos actuales
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, engine)
            
            # Convierte a CSV en memoria
            csv_data = df.to_csv(index=False)
            
            return True, csv_data
            
        except Exception as e:
            return False, f"Error generando CSV: {str(e)}"