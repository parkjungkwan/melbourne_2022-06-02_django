from hello import Member
from hello.domains import my100, myRandom, memberlist


class Quiz00:
    def quiz00calculator(self)-> float:
        a = my100()
        b = my100()
        o = ['+','-','*','/','%']
        o2 = o[myRandom(0,5)]
        if(o2 =='+'):
            c = self.add(a, b)
            print(c)

        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = '홍길동'
        this.height = 170.8
        this.weight = 120.8
        res = this.weight / (this.height * this.height) * 10000
        if res > 25:
            return f'비만'
        elif res > 23:
            return f'과체중'
        elif res > 18.5:
            return f'정상'
        else:
            return f'저체중'

    def quiz02dice(self):
        return myRandom(1, 6)

    def quiz03rps(self):
        c = myRandom(1, 3)
        p = input('가위', '바위', '보')
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        print(' ----------- 1 ------------')
        if p == 1:
            if c == 1:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[1]}, 결과: 패배'
            elif c == '3':
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[2]}, 결과: 승리'
        elif p == 2:
            if c == 1:
                res = '승리'
            elif c == 2:
                res = '무승부'
            elif c == 3:
                res = '패배'
        elif p == 3:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '승리'
            elif c == 3:
                res = '무승부'
        else:
            res = '1~3 입력'
        print(res)
        print(' ----------- 2 ------------')
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '1~3 입력'
        print(res)

    def quiz04leap(self):
        y = myRandom(2000, 2022)
        '''
        s1 = "윤년" if y % 4 == 0 and y % 100 != 0 else "평년"
        s2 = "윤년" if y % 400 == 0 else "평년"
        Java Style => String s = : () ? : ;
        s = (y % 4 == 0 && y % 100 != 0) ? "윤년" : (y % 400 == 0) ? "윤년" : "평년" ;
        Python Style  => s = "" if else ""
        '''
        s = "윤년" if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else "평년"
        

        print(f'{y}년은 {s}입니다.')
        return None
        

    def quiz05grade(self):
        kor = myRandom(0,100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.agv(kor, eng, math)
        grade = self.getGrade()
        passChk = self.passChk()
        return [sum, avg, grade, passChk]

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.kor + self.eng + self.math / 3

    def grade(self):
        pass

    def passChk(self):  # 60점이상이면 합격
        pass

    def quiz06memberChoice(self):
        return memberlist()[myRandom(0, 23)]

    def quiz07lotto(self):
        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        print(Account().to_string())

    def quiz09gugudan(self):  # 책받침구구단
        pass

'''
08번 문제 해결을 위한 클래스는 다음과 같다.
[요구사항(RFP)]
은행이름은 비트은행이다.
입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
예를들면 123-12-123456 이다.
금액은 100 ~ 999 사이로 랜덤하게 입금된다. (단위는 만단위로 암묵적으로 판단한다)
'''
class Account(object):
    def __init__(self):
        self.BANK_NAME = '비트은행'
        self.name = Quiz00().quiz06memberChoice()
        # self.account_number = f'{myRandom(0, 1000):0>3}-{myRandom(0, 100):0>2}-{myRandom(0, 1000000):0>6}'
        self.account_number = self.creat_account_number()
        self.money = myRandom(100, 1000)

    def to_string(self):
        return f'은행 : {self.BANK_NAME}, ' \
               f'입금자: {self.name},' \
               f'계좌번호: {self.account_number},' \
               f'금액: {self.money} 만원'


    def creat_account_number(self):
        ls = [str(i) for i in range(3)]
        ls.append("-")
        return "".join(ls)




