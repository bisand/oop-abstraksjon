from flask import Flask, redirect, render_template, request

from models.BankDatabase import BankDatabase

app = Flask(__name__)

database = BankDatabase()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/transactions", methods=["GET"])
def get_transactions():
    trans = []
    saldo = 0
    for data in database.get_transactions():
        saldo += int(data.amount)
        trans.append(data.__dict__)
    res = {}
    res["saldo"] = saldo
    res["transactions"] = trans
    return render_template("transactions.html", data=res)


@app.route("/transactions", methods=["POST"])
def post_transaction():
    amount = request.form["amount"]
    comment = request.form["comment"]

    if request.form.get("deposit") is not None:
        database.deposit_money(amount, comment)
    elif request.form.get("withdraw") is not None:
        database.withdraw_money(amount, comment)

    return redirect("/transactions")


app.run()
