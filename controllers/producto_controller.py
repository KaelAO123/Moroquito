from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user
import os
from werkzeug.utils import secure_filename
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
        price = float(request.form["price"])
        category = request.form["category"]
        cant_disp = request.form["cant_disp"]
        description = request.form["description"]
        image = request.files["image"]
        
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join('static/images', filename))
            image_path = os.path.join("/images/"+filename)
            print(filename)
        producto:Productos = Productos(name=name, price=price, category=category, cant_disp=cant_disp, description=description,image=image_path)
        producto.save()
        flash("Producto agregado correctamente.", "success")
        return redirect(url_for("product.list_products"))
    return producto_view.create_product()

@product_bp.route("/products/<int:id>/delete")
@login_required
@role_required("admin")
def delete_product(id):
    producto: Productos = Productos.get_by_id(id)
    if not producto:
        return "Producto no encontrado", 404
    producto.delete()
    flash("Producto eliminado correctamente.", "success")
    return redirect(url_for("product.list_products"))


@product_bp.route("/products/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_product(id):
    producto:Productos = Productos.get_by_id(id)
    if not producto:
        return "Producto no encontrado", 404
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        category = request.form["category"]
        cant_disp = request.form["cant_disp"]
        description = request.form["description"]
        image = request.files["image"]
        
        producto.name = name
        producto.price = price
        producto.category = category
        producto.cant_disp = cant_disp
        producto.description = description
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join('static/images', filename))
            image_path = os.path.join("/images/"+filename)
            print(filename)
        producto.image = image_path
        
        flash("Producto actualizado exitosamente", "success")
        producto.save()
        return redirect(url_for("product.list_products"))

    return producto_view.update_product(producto)