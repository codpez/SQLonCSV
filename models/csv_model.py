from sqlalchemy import create_engine
import os
class CSVModel:
    def __init__(self):
        """
        Modelo para manejar los datos del CSV y su estado en la base de datos
        """
        self.engine = None
        self.columns = None
        self.filename = None
        self.table_name = None
        self.total_rows = 0


    # En CSVModel
    def initialize_db(self):
        """Inicializa la conexión a la base de datos"""
        # Crear directorio si no existe
        os.makedirs('database', exist_ok=True)
        # Crear la base de datos en el directorio
        self.engine = create_engine('sqlite:///database/database.db')
        return self.engine
        
    def store_dataframe(self, df, filename):
        """Almacena el DataFrame en la base de datos- pasa los datos del df del csv a la DB"""
        self.filename = filename
        self.table_name = os.path.splitext(filename)[0].lower()
        self.table_name = ''.join(c if c.isalnum() else '_' for c in self.table_name)
        self.columns = df.columns.tolist()
        self.total_rows = len(df)
        df.to_sql(self.table_name, self.engine, if_exists='replace', index=False)
    
    def get_table_info(self):
        """Retorna información sobre la tabla actual"""
        return {
            "filename": self.filename,
            "columns": self.columns,
            "total_rows": self.total_rows
        }
    
    def get_engine(self):
        """
        Retorna el engine de SQLAlchemy actual
        """
        return self.engine