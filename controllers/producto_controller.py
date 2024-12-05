from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

from views import producto_view

from models.producto_model import Productos

from utils.decorators import role_required

product_bp = Blueprint("product",__name__)

@product_bp.route("/productos", methods=["GET", "POST"])
@login_required
def list_products():
    productos: Productos = Productos.get_all()
    return producto_view.list_products(productos)

@product_bp.route("/productos/create", methods=["POST","GET"])
@login_required
@role_required("admin")
def create_product():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        category = request.form["category"]
        cant_disp = request.form["cant_disp"]
        description = request.form["description"]
        producto:Productos = Productos(name=name, price=price, category=category, cant_dis=cant_disp, description=description)
        producto.save()
        flash("Producto agregado correctamente.", "success")
        return redirect(url_for("producto.list_products"))
    return producto_view.create_product()

@product_bp.route("/productos/<int:id>/delete")
@login_required
@role_required("admin")
def delete_product(id):
    producto: Productos = Productos.get_by_id(id)
    if not producto:
        return "Producto no encontrado", 404
    producto.delete()
    flash("Producto eliminado correctamente.", "success")
    return redirect(url_for("producto.list_products"))
