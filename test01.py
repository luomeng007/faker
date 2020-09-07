# -*- coding: utf-8 -*-
from faker import Faker
"""
we could use this modules to create fake information.
"""


class createFakeInformation:
    def mainProgram(self):
        # set the output is Chinese
        text = Faker('zh_CN')

        __default_num = 10
        
        for i in range(__default_num):
            # create fake name
            print(i+1)
            print("姓名：", text.name())
            # create fake address
            print("地址：", text.address())
            print(' ')


if __name__ == "__main__":
    main = createFakeInformation()
    main.mainProgram()

