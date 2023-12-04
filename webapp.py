from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

expenses = [
    {'id': 1, 'item': 'Pain', 'amount': 3.50},
    {'id': 2, 'item': 'Lait', 'amount': 2.00},
    {'id': 3, 'item': 'Œufs', 'amount': 4.25}
]

def get_expense_by_id(expense_id):
    for expense in expenses:
        if expense['id'] == expense_id:
            return expense
    return None

@app.route('/')
def show_expenses():
    return render_template('expenses.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        item = request.form['item']
        amount = float(request.form['amount'])
        new_id = max([expense['id'] for expense in expenses]) + 1
        new_expense = {'id': new_id, 'item': item, 'amount': amount}
        expenses.append(new_expense)
        return redirect(url_for('show_expenses'))
    return render_template('add_expense.html')

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    expense = get_expense_by_id(expense_id)
    if expense:
        expenses.remove(expense)
    return redirect(url_for('show_expenses'))

if __name__ == '__main__':
    app.run(debug=True)
