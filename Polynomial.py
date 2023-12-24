class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    # Operation 1: Insertion
    def insert(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if not self.head or self.head.exponent < exponent:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.exponent > exponent:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # Operation 2: Deletion
    def delete(self, exponent):
        current = self.head
        prev = None
        while current and current.exponent != exponent:
            prev = current
            current = current.next
        if prev and current:
            prev.next = current.next
        elif current:
            self.head = current.next

    # Operation 3: Printing
    def print_polynomial(self):
        current = self.head
        poly_str = ""
        while current:
            poly_str += f"{current.coefficient}x^{current.exponent}"
            current = current.next
            if current:
                poly_str += " + "
        print(poly_str if poly_str else '0')

    # Operation 4: Addition (placeholder)
    def add(self, other):
        print("Addition operation is not implemented in this example.")

    # Operation 5: mnl (placeholder)
    def mnl(self):
        print("MNL operation is a placeholder and has not been defined.")

# Hashing function to map operation number to function
operation_map = {
    1: Polynomial.insert,
    2: Polynomial.delete,
    3: Polynomial.print_polynomial,
    4: Polynomial.add,
    5: Polynomial.mnl,
}

# Initialize polynomial
polynomial = Polynomial()

# Main program
def main():
    while True:
        print("\nOperations:")
        print("1: Insert a term (coefficient, power)")
        print("2: Delete a term (power)")
        print("3: Print polynomial expression")
        print("4: Add another polynomial (not implemented)")
        print("5: MNL operation (not defined)")
        print("6: Departure (exit program)")
        
        try:
            operation = int(input("Enter operation number (1-6): "))
            if operation == 6:
                print("Exiting program.")
                break
            if operation in operation_map:
                if operation == 1:
                    c = float(input("Enter coefficient: "))
                    p = int(input("Enter power: "))
                    operation_map[operation](polynomial, c, p)
                elif operation == 2:
                    p = int(input("Enter power of term to delete: "))
                    operation_map[operation](polynomial, p)
                elif operation == 3:
                    operation_map[operation](polynomial)
                else:
                    operation_map[operation](polynomial)
            else:
                print("Invalid operation number.")
        except ValueError as e:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()