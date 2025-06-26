from flask import Flask, render_template, request, redirect, url_for
from modelo import Producto, guardar_producto, obtener_productos
from modelo import borrar_productos

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agregar", methods=["POST"])
def agregar_producto():
    nombre = request.form["nombre"]
    categoria = request.form["categoria"]
    precio = float(request.form["precio"])
    
    nuevo_producto = Producto(nombre, categoria, precio)
    guardar_producto(nuevo_producto)
    
    return redirect(url_for("index"))

@app.route("/lista")
def listar_productos():
    productos = obtener_productos()
    return render_template("lista.html", productos=productos)


@app.route("/borrar")
def borrar():
    borrar_productos()
    return redirect(url_for("listar_productos"))


if __name__ == "__main__":
    app.run(debug=True)