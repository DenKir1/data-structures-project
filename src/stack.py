class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack(Node):
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.count = 0
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data)
        node.data = data
        node.next_node = self.top
        self.top = node
        self.count += 1


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        top = self.top.data
        self.top = self.top.next_node
        self.count -= 1
        return top
