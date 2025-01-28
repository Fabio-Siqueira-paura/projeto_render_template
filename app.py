from flask import Flask, render_template
import random

app =  Flask(__name__)

# lista de cores
lista_cores = ["red",
               "blue",
               "#FACADA",
               "#BABACA",
               "#00FF00",
               "aqua",
              " green",
              "Yellow",
              "Pink",
              "black"]


# rotas
@app.route("/sobre")
def pag_sobre():
    cor_fundo = random.choice(lista_cores)
    return render_template("sobre.html", cor_fundo_html = cor_fundo)






app.run(debug = True)