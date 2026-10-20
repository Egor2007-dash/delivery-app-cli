class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []
        self.status = "Создан"

    def add_item(self, item_name, price):
        self.items.append({"name": item_name, "price": price})
        print(f"Товар '{item_name}' добавлен в заказ №{self.order_id}.")

    def calculate_total(self):
        total = sum(item["price"] for item in self.items)
        return total

    def update_status(self, new_status):
        self.status = new_status
        print(f"Статус заказа №{self.order_id} изменен на: {self.status}")
# Пример использования:
if __name__ == "__main__":
    # Создаем новый заказ
    my_order = Order(101, "Егор")
    
    # Добавляем товары
    my_order.add_item("Пицца Пепперони", 650)
    my_order.add_item("Кола", 150)
    
    # Считаем общую стоимость
    total_cost = my_order.calculate_total()
    print(f"Общая сумма заказа: {total_cost} руб.")
    
    # Меняем статус
    my_order.update_status("Доставляется")