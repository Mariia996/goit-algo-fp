class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data: int):
        """Функція вставки вузла на початок однозв'язного списку."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: int):
        """Функція вставки вузла в кінець однозв'язного списку."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data: int):
        """Функція вставки вузла після вказаного вузла однозв'язного списку."""
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        """Функція видалення вузла з однозв'язного списку."""
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            raise ValueError(f"Вузол із значенням {key} не знайдено.")
        prev.next = cur.next

    def search_element(self, data: int) -> Node | None:
        """Функція пошуку вузла в однозв'язному списку."""
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        raise LookupError(f"Елемент {data} не знайдено.")

    def print_list(self):
        """Функція виведення однозв'язного списку на екран."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Функція реверсування однозв'язного списку, яка змінює посилання між вузлами."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self, head: Node) -> Node:
        """Aлгоритм сортування (функція) для однозв'язного списку."""
        if not head or not head.next:
            return head
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        return self.sorted_merge(left, right)

    def sort(self):
        """Обгортка для запуску merge_sort з голови списку."""
        self.head = self.merge_sort(self.head)

    def get_middle(self, head):
        """Функція, що знаходить середній вузол однозв'язного списку."""
        if not head:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, a, b):
        """Функція, що об`єднує два відсортовані однозв'язні списки в один відсортований список."""
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result


def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    """Функція, що об`єднує два відсортовані однозв'язні списки в один відсортований список."""
    dummy = Node(0)
    tail = dummy
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1:
        tail.next = current1
    if current2:
        tail.next = current2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


ll1 = LinkedList()
for value in [10, 2, 5, 6, 3]:
    ll1.insert_at_end(value)

print("Початковий список:")
ll1.print_list()
# 10 -> 2 -> 5 -> 6 -> 3 -> None

print("Реверсований список:")
ll1.reverse()
ll1.print_list()
# 3 -> 6 -> 5 -> 2 -> 10 -> None

print("Відсортований список:")
ll1.sort()
ll1.print_list()
# 2 -> 3 -> 5 -> 6 -> 10 -> None

ll2 = LinkedList()
for value in [4, 1, 6]:
    ll2.insert_at_end(value)
ll2.sort()

print("Об'єднання двох відсортованих списків:")
merged = merge_sorted_lists(ll1, ll2)
merged.print_list()
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 6 -> 10 -> None