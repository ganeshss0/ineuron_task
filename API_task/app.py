from flask import Flask, request, jsonify, render_template
import pandas as pd
app = Flask(__name__)

def get_items() -> 'list[dict]':
    items = []
    for i in range(1, 7):
        item_name = request.form[f'item-{i}']
        item_cost = request.form[f'cost-{i}']
        items.append({'Name':item_name, 'Price' : float(item_cost)})
    return items

def get_discount(total_bill: int):
    discount = 0
    if 500 < total_bill <= 1000:
        discount = 0.1
    elif 1000 < total_bill <= 2000:
        discount = 0.2
    elif total_bill > 2000:
        discount = 0.3
    
    return str(discount * 100)+'%', discount * total_bill * -1
    
@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/checkout', methods = ['POST'])
def CheckOut():
    items = get_items()
    bill = pd.DataFrame(items, index = [1, 2, 3, 4, 5, 6])
    total = bill.Price.sum()
    
    discount = get_discount(total)
    total += discount[1]
    result = [{'Name':'', 'Price': ''}, {'Name': f'Discount({discount[0]})', 'Price' : discount[1]}, {'Name': 'Total', 'Price': total}]
    total_amount = pd.DataFrame(result, index = ['', '*', '*'])
    bill = pd.concat((bill, total_amount))
    return bill.to_html(justify='center')
    









if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)