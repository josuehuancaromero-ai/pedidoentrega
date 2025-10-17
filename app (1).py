from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "mi_clave_secreta"  # Necesario para sesiones y flash

# Usuario de prueba
users = {
    "1234": {"password": "1234", "role": "admin"},
    "Angelo": {"password": "4321", "role": "editor"},
    "Patrick": {"password": "4444", "role": "usuario"}
}

@app.route('/')
def home():
    return redirect(url_for('login'))  # Redirige automáticamente al login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificación de usuario
        if username in users and users[username]['password'] == password:
            session['username'] = username
            session['role'] = users[username]['role']
            flash('¡Has iniciado sesión correctamente!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Debes iniciar sesión primero', 'warning')
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
