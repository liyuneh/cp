class Main:
    def sorted(self, list1):
        for i in range(1, len(list1)):
            if list1[i-1] <= list1[i]:
                return True
            else:
                return False
q = Main()
user_input = (input("Enter the number with space :"))
list1 = list(map(int, user_input.split()))
if q.sorted(list1):
    print("True")
else:
    print("False")

