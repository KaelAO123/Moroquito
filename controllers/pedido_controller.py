
from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from views import pedido_view
from models.pedido_model import Pedidos
from models.producto_model import Productos
from models.usuario_model import Usuarios
from utils.decorators import role_required
from datetime import datetime

pedido_bp = Blueprint("pedido",__name__)

@pedido_bp.route("/pedidos/create", methods=["POST","GET"])
@login_required
def create_pedido():
    if request.method == "POST":
        fecha_pedido = datetime.now()
        direction = request.form["direction"]
        message = request.form["message"]
        idProduct = int(request.form["idProduct"])
        email = request.form["email"]
        cantidadPedida = int(request.form["cantidadPedida"])
        fecha_entrega = datetime.strptime(request.form["fecha_entrega"] , '%Y-%m-%dT%H:%M')
        if not message:
            message = ""
        pedido:Pedidos = Pedidos(
            fecha_pedido=fecha_pedido,
            fecha_entrega=fecha_entrega,
            direction=direction,
            email=email,
            idProduct=idProduct,
            message=message,
            cantidadPedida=cantidadPedida)
        pedido.save()
        flash("Pedido agregado correctamente.", "success")
    return redirect(url_for("product.list_products"))

@pedido_bp.route("/pedidos", methods=["GET", "POST"])
@login_required
def list_pedidos():
    pedidos = Pedidos.join(Productos,current_user.email)
    for pedido, product in pedidos:
        print(pedido.idPedido, product.name, product.image)
    return pedido_view.list_pedidos(pedidos)

@pedido_bp.route("/pedidos/<int:id>/update", methods=["GET", "POST"])
@login_required
def update_pedido(id):
    pedido:Pedidos = Pedidos.get_by_id(id)
    if not pedido:
        return "Producto no encontrado", 404
    if request.method == "POST":
        direction = request.form["direction"]
        message = request.form["message"]
        cantidadPedida = int(request.form["cantidadPedida"])
        fecha_entrega = datetime.strptime(request.form["fecha_entrega"] , '%Y-%m-%dT%H:%M')
        
        pedido.direction = direction
        pedido.fecha_entrega = fecha_entrega
        pedido.message = message
        pedido.cantidadPedida = cantidadPedida
        pedido.fecha_pedido = datetime.now()
        flash("Producto actualizado exitosamente", "success")
        pedido.save()
        return redirect(url_for("pedido.list_pedidos"))

    return pedido_view.update_pedido(pedido)

@pedido_bp.route("/pedidos/<int:id>/delete")
@login_required
def delete_pedido(id):
    pedido: Pedidos = Pedidos.get_by_id(id)
    if not pedido:
        return "Producto no encontrado", 404
    pedido.delete()
    flash("Pedido eliminado correctamente.", "success")
    return redirect(url_for("pedido.list_pedidos"))