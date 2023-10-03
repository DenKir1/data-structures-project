class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = self.tail = node  # голова и хвост ссылается на единственный элемент

        else:
            node.next_node = self.head
            self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = self.tail = node  # голова и хвост ссылается на единственный элемент
        else:

            self.tail.next_node = node
            self.tail = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        node = self.head
        list_node = []
        while node:
            list_node.append(node.data)
            node = node.next_node
        return list_node

    def get_data_by_id(self, id_):
        res = None
        node = self.head
        while node:
            a = node.data
            try:
                if id_ == a['id']:
                    res = node.data
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
            node = node.next_node
        return res
