def func_with_knowly(a, b=42, *args, c, d=256, **kwargs):
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('args:', args)
    print('kwargs:', kwargs)

func_with_knowly(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F')
func_with_knowly(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F')
