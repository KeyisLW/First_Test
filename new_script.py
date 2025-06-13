def celsius_to_fahrenheit(celsius):
    """将摄氏度转换为华氏度"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """将华氏度转换为摄氏度"""
    return (fahrenheit - 32) * 5/9

def main():
    print("温度转换工具")
    print("1. 摄氏度 -> 华氏度")
    print("2. 华氏度 -> 摄氏度")
    
    choice = input("请选择转换类型 (1/2): ")
    
    if choice == '1':
        celsius = float(input("请输入摄氏度: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C 等于 {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("请输入华氏度: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F 等于 {celsius}°C")
    else:
        print("无效的选择，请输入1或2")

if __name__ == "__main__":
    main()    