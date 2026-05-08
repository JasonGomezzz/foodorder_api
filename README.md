# 🍔 FoodOrder API

API REST para gestión de restaurante: administración de menús y pedidos de clientes.

## 🛠️ Tecnologías
- Python 3.x
- Django 6.0.5
- Django REST Framework

## ▶️ Instrucciones para ejecutar

```bash
git clone https://github.com/JasonGomezzz/foodorder_api.git
cd foodorder_api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 📡 Endpoints

### Platos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/platos/` | Lista todos los platos |
| POST | `/api/platos/` | Crea un plato |
| PUT | `/api/platos/{id}/` | Actualiza un plato |
| DELETE | `/api/platos/{id}/` | Elimina un plato |
| GET | `/api/platos/?search=postre` | Busca por nombre o categoría |

### Pedidos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/pedidos/` | Lista pedidos con platos anidados |
| POST | `/api/pedidos/` | Crea un pedido |
| PUT | `/api/pedidos/{id}/` | Actualiza un pedido |
| DELETE | `/api/pedidos/{id}/` | Elimina un pedido |
| GET | `/api/pedidos/?search=pendiente` | Busca por estado |

## 📝 Ejemplos de uso

### Crear Plato
```json
POST /api/platos/
{
    "nombre": "Lomo Saltado",
    "precio": "25.00",
    "categoria": "principal"
}
```

### Crear Pedido
```json
POST /api/pedidos/
{
    "total": "30.00",
    "estado": "pendiente",
    "platos": [1, 2]
}
```

### Respuesta GET /api/pedidos/ (relación + punto extra)
```json
{
    "id": 1,
    "fecha": "2026-05-08T10:00:00Z",
    "total": "30.00",
    "estado": "pendiente",
    "platos": [1, 2],
    "platos_detalle": [
        {"id": 1, "nombre": "Lomo Saltado Especial", "precio": "28.00", "categoria": "principal"},
        {"id": 2, "nombre": "Inca Kola", "precio": "5.00", "categoria": "bebida"}
    ]
}
```