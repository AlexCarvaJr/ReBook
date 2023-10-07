from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def rebook():
    return render_template('catalogo.html')

@app.route('/anseios' , methods=['GET'])
def irParaContoI():
    nomeDoConto = request.form.get('nomeDoConto')
    return render_template('anseios.html')

@app.route('/seisirmaos' , methods=['GET'])
def irParaContoII():
    nomeDoConto = request.form.get('nomeDoConto')
    return render_template('seisirmaos.html')

@app.route('/forca' , methods=['GET'])
def irParaContoIII():
    nomeDoConto = request.form.get('nomeDoConto')
    return render_template('forca.html')

@app.route('/atorredourada' , methods=['GET'])
def irParaContoIV():
    nomeDoConto = request.form.get('nomeDoConto')
    return render_template('atorredourada.html')

@app.route('/quandovocepartiu' , methods=['GET'])
def irParaContoV():
    nomeDoConto = request.form.get('nomeDoConto')
    return render_template('quandovocepartiu.html')

@app.route('/onovobrasil' , methods=['GET'])
def irParaContoVI():
    nomeDoConto = request.form.get('nomeDoConto')
    return render_template('onovobrasil.html')

@app.route('/osoutros' , methods=['GET'])
def irParaContoVII():
    nomeDoConto = request.form.get('nomeDoConto')
    return render_template('osoutros.html')

@app.route('/afamilianonorte' , methods=['GET'])
def irParaContoVIII():
    nomeDoConto = request.form.get('nomeDoConto')
    return render_template('afamilianonorte.html')

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
