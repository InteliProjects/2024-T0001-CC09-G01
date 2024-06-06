def calculate_current_price(purchases_quantities, purchases): # ((preco, quantidade), (preco, quantidade), ...)
    total_price = 0
    total_quantity = 0

    for purchase in range(len(purchases_quantities)):
        total_price += purchases.iloc[purchase]["Preço"] * purchases_quantities[purchase]
        print("total_price" + str(total_price))
        total_quantity += purchases_quantities[purchase]
        print("total_quantity" + str(total_quantity))  


    if total_quantity == 0:
      return 0

    return float(format(total_price / total_quantity, '.2f')) # Formatado para 2 casas decimais a fim de
    # simplificar mock dos testes 


def calculate_ideal_price(sale_price, du, di):
  #pi=pv/(di+1)^du/252
  ideal_price = sale_price / ((di + 1) ** (du / 252))
  return ideal_price

def calculate_cdi(du, purchase_price, sale_price, di):
    if purchase_price == 0:
      return 0
    rent = ((sale_price / purchase_price) - 1)
    annual_rent = ((1 + rent) ** (252 / du)) - 1

    cdi = (annual_rent / di) * 100

    return cdi