obj= ["책상" ,"서랍", "액자" ,"전화기", "화분" ,"문"]
desklist=["피리" , "와인잔" ]
timelist={10:"밤이되었다.\n찍! 찍! \n 쥐떼다 ! 쥐를 진정시켜야해." ,
          2: " 낮이되었다.\n 화분에서 소리가 난 것 같다. " ,
          6: " 창문을 보니 해가 지고 있다. \n 창문을 따라 그림자가 져있다."}
call = ["u","a","m","c","e","o","t","s"]

import turtle
t = turtle.Turtle()
s= turtle.Screen()

image_name = ["C:\\Users\\yyjj6\\Desktop\\이미지\\기본방.gif",
              "C:\\Users\\yyjj6\\Desktop\\이미지\\전화기.gif",
              "C:\\Users\\yyjj6\\Desktop\\이미지\\피리부는소년.gif",
              "C:\\Users\\yyjj6\\Desktop\\이미지\\화분.gif",
              "C:\\Users\\yyjj6\\Desktop\\이미지\\쪽지.gif",
              "C:\\Users\\yyjj6\\Desktop\\이미지\\와인.gif",
              "C:\\Users\\yyjj6\\Desktop\\이미지\\없는화분.gif",
              "C:\\Users\\yyjj6\\Desktop\\이미지\\배드엔딩1.gif",
              "C:\\Users\\yyjj6\\Desktop\\이미지\\배드엔딩2.gif",
              "C:\\Users\\yyjj6\\Desktop\\이미지\\성공.gif",
              "C:\\Users\\yyjj6\\Desktop\\이미지\\시계.gif"]

s.setup(700, 700)
s.addshape(image_name[0])
s.addshape(image_name[1])
s.addshape(image_name[2])
s.addshape(image_name[3])
s.addshape(image_name[4])
s.addshape(image_name[5])
s.addshape(image_name[6])
s.addshape(image_name[7])
s.addshape(image_name[8])
s.addshape(image_name[9])
s.addshape(image_name[10])

def clock(time):
    if time == 10 :
         print("\n%s\n"%timelist[time])
         global p
         p+=1
         wine()
    elif time == 2 :
         print("\n%s\n"%timelist[time])
         global eat
         eat+=1
         wine()
    elif time == 6:
         print("\n%s\n"%timelist[time])
         print(" 그림자가"+secret[1]+"처럼 보인다.\n")
         wine()
    else:
        print("\n 아무일도 일어나지 않았다.\n")

def wine():
    if key >= 1:
        t.shape(image_name[5])
    else:
        t.shape(image_name[0])

def enter():
    a=(input("뒤로가려면 아무 숫자나 입력하세요."))
        

p=0 #피리
key=0
glass = 0 #와인잔
ten = 0 #10시
eat = 0 # 화분
chance = 10

import random
secretLen = 3

secretList = random.sample(range(10),secretLen)
secret = ""
for i in range(secretLen):
    secret += str(secretList[i])



print ( "당신은 어떤 방 안에 갇혔습니다.\n방안을 잘 살펴 비밀번호를 찾고, 탈출하세요.\n" )
print ( "\n뒤로가려면 0을 입력하시면 됩니다.\n" )

while True:
    wine()
    print()
    print (obj)
    o = input( " 위의 물체들 중에 어떤 것을 보시겠습니까? : " )

    
    if o == "책상" :
        print ( " \n 책상 위에는"+str(desklist)+"이(가) 있다. \n" )
        desk = input ( "어느것을 보시겠습니까? : ")
        if desk == "피리":
            if p >= 1 :
               print(" \n필릴릴리~ \n 쥐들이 진정했다. \n 쥐는" + secret[2] + "마리가 있다.\n " )
               del(obj[0])
            else:
                print ("\n필릴릴리~ \n아무일도 일어나지 않았다.\n")
                print ()
                continue
            
        if desk == "와인잔":
            print()
            glass= int(input( "\n와인잔에 정체모를 포도주가 담겨있다. 어떡할까? \n 1. 마신다 2. 버린다. ( 번호입력 ): "))
            
            if glass == 1 :
                print()
                print ( " \nBAD ENDING! \n 당신은 독이 담긴 포도주를 마시고 사망했습니다. " )
                t.shape(image_name[7])
                break
                
            if glass == 2 :
                print(" \n 포도주를 버렸다. \n 쨍그랑! 열쇠가 떨어졌다. \n 열쇠를 획득했다.\n")
                key += 1
                del(desklist[1])
                continue
            else :
                print("\n 당신은 아무 행동도 하지 않았습니다.\n")
                
    if o == "서랍" :

        print()
        chest = int(input(" 1. 첫번째 칸 2. 두번째칸 (번호입력) : " ))

        if chest == 1:
            t.shape(image_name[4])
            print ( " \n 쪽지다. \n < 8 - 야옹 = ? > 과 시계가 그려져있다. " )
            enter()
            continue
        if chest == 2:
            print( " \n 잠겨있다. " )
            if key == 1 :
                print(" \n열쇠로 서랍을 풀었다.\n" )
                t.shape(image_name[10])
                clock(time = int(input ( " 안에 시계가 있다. \n 시침을 조정할 수 있다. 몇시로 할까? ( 돌아가기 = 0 ) : " )))
                enter()
                continue
            
    if o == "액자" :
        t.shape(image_name[2])
        print( " \n 벽에 커다란 액자가 걸려있다. \n 아이가 그린 것 같다. \n 피리부는 아이와 고양이와 쥐가 사이좋게 걸어가고 있다. \n")
        enter()
        continue
    
    if o == "전화기":
        t.shape(image_name[1])
        print()
        print(call)
        print ("\n 전화기에 숫자가 아닌 알파벳이 적혀있다. \n 조합해서 입력해 전화를 걸어보자.\n 조합되는 단어는 총 2개다. 한 단어씩 입력하자.\n " )
        calling = input(" 단어입력 :" )
        if calling == "mouse":
            print("\n뚜두두..\n \n 뚜두두... \n \n 찍.. 찍..! \n 쥐는 10시를 좋아해." )
            enter()
            continue
        if calling == "cat" :
            print("\n뚜두두..\n \n 뚜두두... \n \n 야옹~ \n 고양이는 2시를 좋아해." )
            enter()
            continue
        else :
            print("\n뚜두두..\n \n 뚜두두... \n \n 아무일도 일어나지 않았다." )
            enter()
            continue
        
    if o == "화분" :
        if eat >= 1 :
            t.shape(image_name[3])
            print ("\n사람 키만한 초록색 식물이다. \n 열매가 " +secret[0]+"개 떨어져 있다.\n" )
            enter()
            continue
        else:
            t.shape(image_name[6])
            print("\n사람 키만한 초록색 식물이다. 그게 다인 것 같다.\n" )
            enter()
            continue
        
    if o == "문" :
        print ( "\n이 문으로 나가면 될 것 같다. 비밀번호가 걸려있다.\n 기회는 10번 뿐이다. \n" )
        yon = int (input ( " 입력하시겠습니까? 예(1) , 아니오 (2) ( 번호입력 ) : " ))
        if yon == 1 :
        
            password = input ( "\n비밀번호 세자리를 입력하시오 : " )
            if password == secret and chance >0 :
                print (" \n 비밀번호 일치!\n 탈출을 성공하셨습니다." )
                t.shape(image_name[9])
                break
            elif password != secret and chance > 0 :
                print (" \n 비밀번호 불일치!\n 다시 시도하세요. " )
                chance -= 1
                continue
            else :
                print (" \n BAD ENDING! \n 당신은 탈출을 실패했습니다. 방안에서 당신은 아사합니다. " )
                t.shape(image_name[8])
        else :
            continue
            
        
