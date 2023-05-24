

class Polynomial:
    def __init__(self, *args, **kwargs):

        self.numbers=[] # cisla
        
        for i in args:
            if type(i) is list: # kdyz dostanu vypis pomoci listu a ne jako argumenty
                self.numbers = i 
                
        if len(self.numbers) == 0: # kdyz je mam prazdnej list
            if args:
                self.numbers=list(args) 
                
            elif kwargs:
                for x,value in kwargs.items():
                    for i in range(1 + int(x.split("x")[1]) - len(self.numbers)): # todle...
                        self.numbers.append(0)

                    self.numbers[int(x.split("x")[1])] = value
            else: 
                print('nemam argumenty ani kwargs')
                return 0
            
        for i in range(len(self.numbers)-1, 0, -1): # vymaz prebytecnych nul v nejvyssich mocninach
            if self.numbers[i]==0:
                del self.numbers[i]
            else:
                break # pokud narazime na nenulovou hodnotu, neni treba pokracovat

    def __str__(self):
        power = 0 
        printarr = []
        if (self.numbers == [0,0,0]): return '0'; # osetreno 10/10 programator
        if (self.numbers == [0,0]): return '0'; 
        if (self.numbers == [0]): return '0'; 
        for arg in self.numbers: 
            if (arg != 0) :
                if (arg < 0) : 
                    if (power == 1) :
                        if (arg == -1) :
                            temp = 'x'
                        else:
                            temp = str(arg * -1) + 'x' 
                    elif (power == 0) :
                        temp = str(arg * -1)
                    else :
                        if (arg == -1) :
                            temp = 'x' + '^' + str(power)
                        else:
                            temp = str(arg * -1) + 'x' + '^' + str(power)

                    printarr.insert(0, temp)
                    printarr.insert(0, '-' if arg < 0 else '+')


                else : 
                    if (power == 0) :
                        temp = str(arg)
                    
                    else :
                        if (power == 1) :
                            if (arg == 1) :
                                temp = 'x'
                            else:
                                temp = str(arg) + 'x' 
                        else :
                            if (arg == 1) :
                                temp = 'x' + '^' + str(power)
                            else:
                                temp = str(arg) + 'x' + '^' + str(power)
                
                    printarr.insert(0, temp)
                    printarr.insert(0, '+')
            power += 1

        stringArr = ' '.join(map(str, printarr))
        stringArr = stringArr[2:]
        return stringArr
    
    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.numbers == other.numbers
        else: 
            return '0'
    
    def __add__(self, other):
        # if not isinstance(other, Polynomial):
            # other = Polynomial(other)
        res_numbers = [0] * max(len(self.numbers), len(other.numbers))
        for i in range(len(self.numbers)):
            res_numbers[i] += self.numbers[i]
        for i in range(len(other.numbers)):
            res_numbers[i] += other.numbers[i]
        return Polynomial(*res_numbers)
    
    def __pow__(self, n):
        if n < 0: raise ValueError("n < 0") 
        
        if n == 0: 
            return Polynomial(1)

        result = Polynomial(self.numbers) # [-1, 1]
        for i in range(n - 1): 
            result = result * Polynomial(self.numbers) # nasobime pomoci mul

        return result
    
    def __mul__(self, secondnum):
        # if not isinstance(secondnum, Polynomial):
        #     secondnum = Polynomial(secondnum)
        res_numbers = [0] * (len(self.numbers) + len(secondnum.numbers) - 1) # array stejna delka ale filled with 0s

        for i in range(len(self.numbers)):
            for j in range(len(secondnum.numbers)):
                res_numbers[i + j] += self.numbers[i] * secondnum.numbers[j] # kazdy s kazdym


        return Polynomial(res_numbers)
    
    def derivative(self):
        result = [0] * (len(self.numbers) - 1) # zas naplnim nulama

        for i in range(1, len(self.numbers)):
            result[i - 1] = i * self.numbers[i]

        if (len(result)) == 0: return 0
        else: return Polynomial(result)
    
    def at_value(self, x, y = 0):
        resultY = 0
        if (y > 0): # kdyz mam y, pocitam i y
            resultY = 0
            for i in range(len(self.numbers)):
                resultY += self.numbers[i] * y ** i

        resultX = 0
        for i in range(len(self.numbers)):
            resultX += self.numbers[i] * x ** i

        if (y > 0): return resultY - resultX
        else: return resultX

def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x" #
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5" #
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x" #
    assert str(Polynomial(x2=0)) == "0" #
    assert str(Polynomial(x0=0)) == "0" #
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3) #
    assert Polynomial(x2=0) == Polynomial(x0=0) #
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1" #
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2" # 
    pol1 = Polynomial(x2=3, x0=1) # 
    pol2 = Polynomial(x1=1, x3=0) # 
    assert str(pol1+pol2) == "3x^2 + x + 1" # 
    assert str(pol1+pol2) == "3x^2 + x + 1" #
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1" #
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1" #
    pol3 = Polynomial(x0=-1,x1=1) #
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1" #
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1" #
    assert str(Polynomial(x0=2).derivative()) == "0" #
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3" #
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x" #
    pol4 = Polynomial(x3=2,x1=3,x0=2) #
    assert str(pol4.derivative()) == "6x^2 + 3" #
    assert Polynomial(-2,3,4,-5).at_value(0) == -2 #
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20 #
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44 #
    pol5 = Polynomial([1,0,-2]) #
    assert pol5.at_value(-2.4) == -10.52 #
    assert pol5.at_value(-2.4) == -10.52 #
    assert pol5.at_value(-1,3.6) == -23.92 #
    assert pol5.at_value(-1,3.6) == -23.92 #

if __name__ == '__main__':
    test() 