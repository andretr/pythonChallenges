from flask import Flask, request, jsonify
from model import FamilyMember

app = Flask(__name__)

familia = {
    1:FamilyMember("mama", {1001: 10000, 1002: 15000}),
2:FamilyMember("papa", {2001: 10000, 2002: 15000}),
3:FamilyMember("hijo"),
4:FamilyMember("hija")}

familia[1].add_hobbies("Correr", "Leer")
familia[2].add_hobbies("Cocinar", "Escuchar musica")
familia[3].add_hobbies("Futbol")
familia[4].add_hobbies("Cantar", "Bailar", "teatro")

@app.route("/familiares/<int:index>/cuentas/")
def get_cuentas(index):
    miembro_familiar = familia[index]
    return jsonify(miembro_familiar.accounts)

@app.route("/familiares/<int:index>/hobbies/")
def get_hobbies(index):
    miembro_familiar = familia[index]
    return jsonify(miembro_familiar.hobbies)

@app.route("/familiares/<int:index>/cuentas/<int:acct_no>")
def get_cuenta(index, acct_no):
    miembro_familiar = familia[index]
    cuenta = miembro_familiar.get_cuenta(acct_no)
    print(cuenta)
    return jsonify(cuenta)

@app.route("/familiares/<int:index>/cuentas/<int:acct_no>/depositar", methods=["POST"])
def post_depositar(index, acct_no, monto):
    miembro_familiar = familia[index]
    cuenta = miembro_familiar.get_cuenta(acct_no)
    return jsonify(cuenta.depositar(cuenta, monto))

@app.route("/familiares/<int:index>/cuentas/<int:acct_no>/retirar", methods=["POST"])
def post_retirar(index, acct_no, monto):
    miembro_familiar = familia[index]
    cuenta = miembro_familiar.get_cuenta(acct_no)
    return jsonify(cuenta.retirar(cuenta, monto))

if __name__ == '__main__':
    app.run(debug=True)
