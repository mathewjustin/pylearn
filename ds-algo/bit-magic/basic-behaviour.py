class BasicBehaviour:


    def showBehaviour(self):

        a = 5 # 0   0    0   1   0   1
        b = 9 # 0   0    1   0   0   1

        #Binary and of 5 and 9
        # 0   0    0   1   0   1 AND
        # 0   0    1   0   0   1
        #-------------------------
        #  0   0     0    0   0   1 =>1

        # The result is 00000001
        print("a = %d, b = %d\n" % (a, b))
        print("a&b = %d\n" % (a & b))

        #Binary and of 5 and 9
        # 0   0    0   1   0   1 OR
        # 0   0    1   0   0   1
        #-------------------------
        #  0   0   1   1   0   1  =>13

        # The result is 00001101
        print("a|b = %d\n" % (a | b))

        #Binary and of 5 and 9
        # 0   0    0   1   0   1 OR
        # 0   0    1   0   0   1
        #-------------------------
        #  0   0   1   1   0   1  =>13 X
        #==>
        #  1    1
        # The result is 00001100
        print("a^b = %d\n" %(a ^ b))

        # The result is 11111010
        print("~a = %d\n" % ~a)

        # The result is 00010010
        print("b<<1 = %d\n" % (b << 1))

        # The result is 00000100
        print("b>>1 = %d\n" %(b >> 1))


if __name__ == '__main__':

    bbehaviour=BasicBehaviour()
    bbehaviour.showBehaviour()