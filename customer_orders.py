"""Модуль для управления данными о клиентах и заказах.

Содержит классы для представления клиентов и заказов, а также функции для расчета скидок и генерации отчетов.
"""


class CustomerDataClass:
    """Класс для представления данных о клиенте."""
    
    def __init__(self, customer_id, customer_name):
        """Инициализирует новый экземпляр клиента.
        
        Args:
            customer_id (int): Уникальный идентификатор клиента
            customer_name (str): Имя клиента
        """
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.orders = []

    def add_order(self, order_object):
        """Добавляет заказ в список заказов клиента.
        
        Args:
            order_object (OrderDataClass): Объект заказа для добавления
        """
        self.orders.append(order_object)

    def get_total_amount(self):
        """Вычисляет общую сумму всех заказов клиента.
        
        Returns:
            float: Общая стоимость всех заказов клиента
        """
        total = 0
        for o in self.orders:
            total = total + o.amount
        return total


class OrderDataClass:
    """Класс для представления данных о заказе."""
    
    def __init__(self, order_id, amount):
        """Инициализирует новый экземпляр заказа.
        
        Args:
            order_id (int): Уникальный идентификатор заказа
            amount (float): Сумма заказа
        """
        self.order_id = order_id
        self.amount = amount


def calculate_discount(customer_obj):
    """Вычисляет размер скидки для клиента на основе общей суммы заказов.
    
    Args:
        customer_obj (CustomerDataClass): Объект клиента
        
    Returns:
        float: Размер скидки (10% от суммы если больше 1000, иначе 0)
    """
    total_amount = customer_obj.get_total_amount()
    discount = total_amount * 0.1 if total_amount > 1000 else 0
    return discount


def print_customer_report(customer_obj):
    """Выводит отчет по клиенту с детальной информацией о заказах.
    
    Args:
        customer_obj (CustomerDataClass): Объект клиента для формирования отчета
    """
    print('Customer Report for:', customer_obj.customer_name)
    print('Total Orders:', len(customer_obj.orders))
    print('Total Amount:', customer_obj.get_total_amount())
    print('Discount:', calculate_discount(customer_obj))
    if len(customer_obj.orders) == 0:
        print('Average Order:', customer_obj.get_total_amount())
    else:
        print('Average Order:', customer_obj.get_total_amount() / len(customer_obj.orders))


def main_program():
    """Основная функция программы, демонстрирующая использование классов.
    
    Создает клиентов и заказы, формирует отчеты.
    """
    c1 = CustomerDataClass(1, 'SAP Customer')
    o1 = OrderDataClass(101, 500)
    o2 = OrderDataClass(102, 800)
    c1.add_order(o1)
    c1.add_order(o2)

    print_customer_report(c1)

    c2 = CustomerDataClass(2, 'Empty Customer')
    print_customer_report(c2)


if __name__ == '__main__':
    main_program()