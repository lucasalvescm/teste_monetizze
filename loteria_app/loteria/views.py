from flask import Flask, render_template, request
from loteria_app.loteria.models import Loteria
from loteria_app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        try:
            result = request.form.to_dict()
            loteria = Loteria(int(result["dezenas"]), int(result["jogos"]))
            loteria.generate_games()
            loteria.generate_lottery()
            result = {
                "table": loteria.get_results(),
                "result": loteria.result,
                "erro": "",
            }
            return render_template("table.html", result=result)
        except Exception as e:
            result = {"table": {}, "result": "", "erro": "Erro: {}".format(str(e))}
            return render_template("table.html", result=result)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
