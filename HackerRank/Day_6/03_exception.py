for _ in range(int(input())):
    try:
        num,den = map(int,input().split())
        res = num//den
        print(res)
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")   
    except ValueError as e:
        print(f"Error Code: {e}")   