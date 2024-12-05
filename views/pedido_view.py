from flask import render_template
from flask_login import current_user


def list_pedidos(pedidos):
    return render_template(
        "pedidos.html",
        pedidos=pedidos,
        title="Lista de Pedidos",
        current_user=current_user,
    )

def create_pedido():
    return render_template(
        "products.html", title="Crear Producto", current_user=current_user
    )

def update_pedido(pedido):
    return render_template(
        "update_pedido.html",
        title="Editar Pedidos",
        pedido=pedido,
        current_user=current_user,
    )