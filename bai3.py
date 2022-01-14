ten = input("Nhập ho ten day du của bạn = ")
print(ten)

def soThuanNghich(n):
    str1 = str(n);  
    str2 = str1[::-1];  
    if (str1 == str2):
        print(n,"là sô thuận nghịch");
    else:
        print(n,"không là sô thuận nghịch");


n = int(input("Nhập số nguyên dương n = "));
print(soThuanNghich(n));
