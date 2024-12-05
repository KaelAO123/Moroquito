from flask import render_template
from flask_login import current_user


# La función `list_animals` recibe una lista de
# animales y renderiza el template `animales.html`
def list_products(products):
    return render_template(
        "products.html",
        products=products,
        title="Lista de products",
        current_user=current_user,
    )

# La función `create_animal` renderiza el
# template `create_animal.html` o devuelve un JSON
# según la solicitud
def create_product():
    return render_template(
        "create_product.html", title="Crear Producto", current_user=current_user
    )

# La función `update_dulce` recibe un dulce
# y renderiza el template `update_dulce.html`
def update_product(product):
    return render_template(
        "update_product.html",
        title="Editar Producto",
        product=product,
        current_user=current_user,
    )