from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

def get_items() -> 'list[dict]':
    items = []
    for i in range(1, 7):
        item_name = request.form[f'item-{i}']
        item_cost = request.form[f'cost-{i}']
        items.append({'Item': i, 'Name':item_name, 'Price' : float(item_cost)})
    return items

def get_discount(total_bill: int):
    discount = 0
    if 500 < total_bill <= 1000:
        discount = 0.1
    elif 1000 < total_bill <= 2000:
        discount = 0.2
    elif total_bill > 2000:
        discount = 0.3
    
    return str(discount * 100)+'%', round(discount * total_bill * -1, 2)
    
@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/checkout', methods = ['POST'])
def CheckOut():
    items = get_items()
    bill = pd.DataFrame(items)
    total = bill.Price.sum()
    
    discount = get_discount(total)
    new_total = round(total + discount[1], 2)
    result = [['Amount', total], [f'Discount({discount[0]})', discount[1]], ['Total',new_total]]

    return render_template('result.html', bill = bill.to_numpy(), amount = result)
    
    # Template.render()








if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)