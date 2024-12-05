from flask import render_template
from flask_login import current_user


# La función `list_animals` recibe una lista de
# animales y renderiza el template `animales.html`
def list_pedidos(pedidos):
    return render_template(
        "pedidos.html",
        pedidos=pedidos,
        title="Lista de Pedidos",
        current_user=current_user,
    )

# La función `create_animal` renderiza el
# template `create_animal.html` o devuelve un JSON
# según la solicitud
def create_pedido():
    return render_template(
        "products.html", title="Crear Producto", current_user=current_user
    )

# La función `update_dulce` recibe un dulce
# y renderiza el template `update_dulce.html`
def update_pedido(pedido):
    return render_template(
        "update_pedido.html",
        title="Editar Pedidos",
        pedido=pedido,
        current_user=current_user,
    )