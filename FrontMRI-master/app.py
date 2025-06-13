from flask import Flask, render_template

# La variable debe llamarse EXACTAMENTE 'app'
app = Flask(__name__)  # <-- Este nombre es crucial

@app.route('/')
def home():
    return render_template('index.html')

# Esto es necesario para que Gunicorn lo detecte correctamente
application = app  # <-- Alias adicional para algunos entornos

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
