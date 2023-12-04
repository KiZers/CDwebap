from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Liste des dépenses initiales
expenses = [
    {'id': 1, 'item': 'Pain', 'amount': 3.50},
    {'id': 3, 'item': 'Œufs', 'amount': 4.25}
]

# Route pour afficher la liste des dépenses
@app.route('/')
def show_expenses():
    return render_template('expenses.html', expenses=expenses)

# Route pour ajouter une nouvelle dépense
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        item = request.form['item']
        amount = float(request.form['amount'])
        new_expense = {'id': len(expenses) + 1, 'item': item, 'amount': amount}
        expenses.append(new_expense)
        return redirect(url_for('show_expenses'))
    return render_template('add_expense.html')

if __name__ == '__main__':
    app.run(debug=True)
