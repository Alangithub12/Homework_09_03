from double_linked_list import LinkedList, Node

class AdvancedLinkedList(LinkedList):

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return "Список выведен с конца"

    def insert_at_index(self, index, data):
        if index == 0:
            return self.insert_at_head(data)
        current_node = self.head
        for i in range(index - 1):
            if current_node is None:
                return self.insert_at_tail(data)
            current_node = current_node.next_node
        if current_node is None:
            return self.insert_at_tail(data)
        new_node = Node(data, current_node, current_node.prev_node)
        if current_node.prev_node:
            current_node.prev_node.next_node = new_node
        current_node.prev_node = new_node
        if new_node.prev_node is None:
            self.head = new_node
        return f"Вставлен узел с данными {data} на индекс {index}"

    def remove_node_index(self, index):
        if index == 0:
            return self.remove_from_head()
        current_node = self.head
        for i in range(index):
            if current_node is None:
                return "Индекс вне диапазона"
            current_node = current_node.next_node
        if current_node is None:
            return "Индекс вне диапазона"
        if current_node.prev_node:
            current_node.prev_node.next_node = current_node.next_node
        if current_node.next_node:
            current_node.next_node.prev_node = current_node.prev_node
        if current_node == self.tail:
            self.tail = current_node.prev_node
        return f"Удален узел с данными {current_node.data} по индексу {index}"

    def remove_node_data(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev_node:
                    current_node.prev_node.next_node = current_node.next_node
                if current_node.next_node:
                    current_node.next_node.prev_node = current_node.prev_node
                if current_node == self.head:
                    self.head = current_node.next_node
                if current_node == self.tail:
                    self.tail = current_node.prev_node
                return f"Удален узел с данными {data}"
            current_node = current_node.next_node
        return "Узел с такими данными не найден"

    def len_ll(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count

    def contains_from_head(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False

    def contains_from_tail(self, data):
        current_node = self.tail
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.prev_node
        return False

    def contains_from(self, data, from_head=True):
        if from_head:
            return self.contains_from_head(data)
        else:
            return self.contains_from_tail(data)