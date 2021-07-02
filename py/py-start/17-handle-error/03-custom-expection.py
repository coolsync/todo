# 在Python中，抛出自定义异常的语法为 raise 异常类对象 。
# 需求：密码长度不足，则报异常（用户输⼊密码，如果输⼊的⻓度不⾜3位，
# 则报错，即抛出自定义异常，并捕获该异常）。


class ShortInputError(Exception):
    def __init__(self, length, min_length) -> None:
        self.length = length
        self.min_length = min_length

    def __str__(self) -> str:
        return f'You input password length is: {self.length}, min length is: {self.min_length}'


def main():
    try:
        con = input('Input passwd: ')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)

    # except Exception:    # alias
    #     print(Exception)
    except Exception as err:    # alias
        print(err)
        
    else:
        print('you input is: %s' % con)


main()
