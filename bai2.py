ten = input("Nhập tên đệm của bạn = ")
print(ten)

def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;


n = int(input("Nhập độ dài tên đệm của bạn n = "));
print("Tổng các chữ số của", n, "là", totalDigitsOfNumber(n));
