import sqlite3
import pandas as pd

# Conexión a la base de datos
conn = sqlite3.connect('clientes_pyme.db')

# Consultar segmentos
df = pd.read_sql_query("SELECT * FROM clientes_segmentados", conn)

print("=== CLIENTES POR SEGMENTO ===")
print(df.groupby('segmento').size())

print("\n=== CLIENTES VIP (Segmento 1) ===")
vip = pd.read_sql_query("""
    SELECT cliente_id, frecuencia_compras, monto_total_usd 
    FROM clientes_segmentados 
    WHERE segmento = 1 
    ORDER BY monto_total_usd DESC
    LIMIT 10
""", conn)
print(vip)

conn.close()
print("\n✅ Consulta completada")