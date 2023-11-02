import uvicorn

from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from typing import Optional

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from fastapi import Request
from fastapi.staticfiles import StaticFiles


# http://127.0.0.1:8000/
app = FastAPI()

# Cargar plantillas HTML
templates = Jinja2Templates(directory="templates")  # Asegúrate de que tu plantilla esté en un directorio llamado "templates"

# Configurar la ruta para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=HTMLResponse)
async def read_menu(request: Request):
    # Renderiza la página de inicio (menu.html) utilizando la plantilla base
    return templates.TemplateResponse("inicio.html", {"request": request})

@app.get("/pagina1", response_class=HTMLResponse)
async def read_pagina1(request: Request):
    # Renderiza la página 1 (pagina1.html) utilizando la plantilla base
    return templates.TemplateResponse("pagina1.html", {"request": request})

@app.get("/pagina2", response_class=HTMLResponse)
async def read_pagina2(request: Request):
    # Renderiza la página 2 (pagina2.html) utilizando la plantilla base
    return templates.TemplateResponse("pagina2.html", {"request": request})

@app.get("/pagina3", response_class=HTMLResponse)
async def read_pagina3(request: Request):
    # Renderiza la página 3 (pagina3.html) utilizando la plantilla base
    return templates.TemplateResponse("pagina3.html", {"request": request})

@app.get("/pagina4", response_class=HTMLResponse)
async def read_pagina4(request: Request):
    # Renderiza la página 4 (pagina4.html) utilizando la plantilla base
    return templates.TemplateResponse("pagina4.html", {"request": request})






if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000) # LocalHost
    uvicorn.run(app, host="0.0.0.0", port=8080)
    #uvicorn.run(app, host="255.255.240.0", port=8000)
    










"""

""" 
# El imput de BaseModel, va a verificar que cada variable sea del tipo que se ha definido: titulo-str, autor-str...
"""
class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]




""" 
# La @ es un decorador, que en python lo que hace es modificar una función. En este caso, simplemente indica la ruta: "/", que será "http://127.0.0.1:8000/"
"""
#@app.get("/")
#def read_root():
#    return {"Hello": "World"}


"""
# Menu
"""

@app.get("/", response_class=HTMLResponse)
async def read_menu(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})

# Define rutas adicionales
@app.get("/pagina1", response_class=HTMLResponse)
async def read_pagina1(request: Request):
    return templates.TemplateResponse("pagina1.html", {"request": request})

@app.get("/pagina2", response_class=HTMLResponse)
async def read_pagina2(request: Request):
    return templates.TemplateResponse("pagina2.html", {"request": request})








@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "greeting": "Hello, World!"})


"""
# Ruta con parámetro: la ruta coge el valor de http://127.0.0.1:8000/items/5 (5), y lo usa dentro de la función.
"""
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




@app.post("/libros")
def insertar_libro(libro: Libro):
    #return {"message": f"libro {libro.titulo} insertado"}
    return templates.TemplateResponse("template.html", {"request": 2})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
"""