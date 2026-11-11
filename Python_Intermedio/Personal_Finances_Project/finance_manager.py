class Category:
    def __init__(self,name:str,color:str="#FFFFFF"):
        self.name = name
        self.color = color
    def to_dict(self):
        """Convierte los atributos de la categoría a un diccionario."""
        return {
            "name": self.name,
            "color": self.color
        }



class Transaction:
    def __init__(self,category:Category,trans_type:str, description:str, amount:float,date):
        self.category = category
        self.trans_type = trans_type
        self.description = description
        self.amount = amount
        self.date = date
    def to_dict(self):
        """Convierte la transacción y su categoría interna a un diccionario."""
        return {
            "trans_type": self.trans_type,
            "description": self.description,
            "amount": self.amount,
            "date": self.date,
            # Aquí anidamos el diccionario de la categoría
            "category": self.category.to_dict()
        }

    
class Income (Transaction):
    def __init__(self, category:Category, description:str, amount:float, date):
        super().__init__(category,"Ingreso", description, amount, date)



class Expense(Transaction):
    def __init__(self, category:Category, description:str, amount:float, date):
        super().__init__(category,"Gasto", description, amount, date)



class  AdmFinance:
    def __init__(self):
        #Aqui se guardaran los movimiento en la memoria del programa
        self.transactions_list =[]
        self.categories = {}


    def add_new_transaction (self, transaction:Transaction):
        self.transactions_list.append(transaction)



    def sum_incomes (self) -> float:
        total=0.0
        for trans in self.transactions_list:
            if trans.trans_type =="Ingreso":
                total += trans.amount
        return total


    def sum_expenses (self) -> float:
        total=0.0
        for trans in self.transactions_list:
            if trans.trans_type == "Gasto":
                total += trans.amount
        return total

    
    def calc_balance (self) -> float:
        balance = self.sum_incomes()-self.sum_expenses()
        return balance