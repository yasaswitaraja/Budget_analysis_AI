from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample AI/logic function
def analyze_budget(income, expenses):
    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    budget_summary = {
        "total_income": income,
        "total_expenses": total_expenses,
        "savings": savings,
        "categories": expenses
    }
    return budget_summary

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    income = data.get("income")
    expenses = data.get("expenses")
    result = analyze_budget(income, expenses)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
