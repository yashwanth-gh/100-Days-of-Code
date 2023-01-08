import random
amount = [ '₹0','₹5,000','₹10,000','₹20,000','₹40,000' ,'₹80,000','₹1,60,000','₹3,20,000','₹6,40,000','₹12,50,000','₹25,00,000','₹50,00,000','₹1 CRORE','₹3 CRORE','₹7 CRORE']
questions =[['1) The Rath Yatra at Puri is celebrated in honour of which Hindu diety?',' a) Lord Ram',' b) Vishnu',' c) Lord Shiva',' d) Jagannath'],
       ['2) For which of the following disciplines Nobel Prize IS NOT awarded?',' a) Physics',' b) Medicine',' c) Mathematics',' d)Literature'],
       ['3) What is the National song of India?',' a) Vande mataram',' b) Jana gana mana',' c) Sare jahan se acha',' d)Maa Tujhe Salaam'],
       ['4) Which city is known as Pink City in India?',' a) Mysuru(Mysore)',' b) Nagpur',' c) Jaipur',' d)Jaisalmer'],
       ['5) Current Railway Minister of India is ?',' a) Ashwini Vaishnaw',' b)Mamta Banarjee',' c) Piyush Goyal',' d)Ram Vilash'],
       ['6) Where in India Gate located?',' a) New delhi',' b) Mumbai',' c) Agra',' d)Kochi'],
       ['7) Which one of the following places is famous for the Great Vishnu Temple?',' a) Bordubar, Indonesia',' b) Ankorvat, Cambodia',' c) Bamiyan, Afghanistan',' d)Panja Sahib, Pakistan'],
       ['8) Taj Mahal was made of this ',' a) Marbel',' b) Sand stone',' c) Granite','d) Limestone brick'],
       ['9) What is made by the churning of whipping cream?',' a) Butter',' b) Cream',' c) Ghee','d) Curd'],
       ['10) MS-Word is an example of which of the following ?',' a) An operating system',' b) A processing device',' c) Application software',' d)An input device'],
       ['11) National Income estimates in India are prepared by',' a) Planning Commission',' b) Reserve Bank of India ',' c) Central statistical organisation',' d)International statistical Institute'],
       ['12) The tropic of cancer does not pass through which of these Indian states ?',' a)  Madhya Pradesh',' b) West Bengal',' c) Rajasthan',' d)Odisha'],
       ['13) The patriotic song ‘Sare Jahan Se Accha’ was composed by:',' a) Bankim Chandra Chatterjee',' b) Bismil Azimabadi',' c) Allama Muhammad Iqbal',' d)Rabindranath Tagore'],     
       ["14) Mahatma Gandhi's remark , ' A post-dated cheque on a crumbling bank' is regarding the proposal of ______",' a) Simon Commission',' b) Cripps Mission',' c) Cabinet Mission',' d)Wavel Plan'], 
       ]
answer = [ ['d',' d) Jaganath'],
          ['c',' c) Mathematics'],
          ['a',' a) Vande amtaram'],
          ['c',' c) Jaipur'],
          ['a', ' a) Ashwini Vaishnaw'],
          ['a', ' a) New delhi'],
          ['b', ' b) Ankorvat, Cambodia'],
          ['a', ' a) Marbel'],
          ['a', ' a) Butter'],
          ['c', ' c) Application software'],
          ['c', ' c) Central statistical organisation'],
          ['d', ' d)Odisha'],
          ['c', ' c) Allama Muhammad Iqbal'],
          ['b', ' b) Cripps Mission']]
wrongans =[[' a) Lord ram',' b) Vishnu', ' c) Lord Shiva'],
           [' a) Physics',' b) Medicine',' d) Literature'],
           [' b) Jana gana mana',' c) Sare jahan se acha',' d) Maa Tujhe Salaam'],
           [' a) Mysuru(Mysore)',' b) Nagpur',' d) Jaisalmer'],
           [' b) Mamta Banarjee',' c) Piyush Goyal',' d) Ram Vilash'],
           [' b) Mumbai',' c) Agra',' d) Kochi'],
           [' a) Bordubar, Indonesia',' c) Bamiyan, Afghanistan',' d)Panja Sahib, Pakistan'],
           [' b) Sand stone',' c) Granite',' d) Limestone brick'],
           [' b) Cream',' c) Ghee',' d)Curd'],
           [' a) An operating system',' b) A processing device',' d) An input device'],
           [' a) Planning Commission',' b) Reserve Bank of India ',' d) International statistical Institute'],
           [' a)  Madhya Pradesh',' b) West Bengal',' c) Rajasthan',],
           [' a) Bankim Chandra Chatterjee',' b) Bismil Azimabadi',' d) Rabindranath Tagore'],
           [' a) Simon Commission', ' c) Cabinet Mission', ' d) Wavel Plan']]
print('*****************************RULES OF GAME****************************')
print('\n-HEY WELCOME TO KBC QUIZ\n-This will be short quiz having 14 Questions\n-This quiz has 14 stages where each stage has a corresponding question that will be asked\n-If you got the correct answer to the question then you will be given money as per the stage\n-Moving up the stages you will be upgrading your money also\n-There will be two safe stage in game where after crossing that particular stage you will be safe with money assigned in tht stage\n-But if you get a question wrong you will be ending the game with money assigned in the previous safe stage\n-You will have two life lines in the game\n(1) 50:50 - Here two wrong option will be removed leaving you with one correct and one wrong option\n(2) 75:25 - here one wrong option will be removed')
print('\n*******************************STAGES*********************************')
print('\n-You can quit the gameplay whenever you want by typing "quit"\n-Here is the detailed levels of game :-')
print('1)      ₹5,000\n2)     ₹10,000\n3)     ₹20,000\n4)     ₹40,000 ------> SAFE STAGE\n5)     ₹80,000\n6)   ₹1,60,000\n7)   ₹3,20,000 ------> SAFE STAGE\n8)   ₹6,40,000\n9)  ₹12,50,000\n10) ₹25,00,000\n11) ₹50,00,000\n12)   ₹1 CRORE\n13)   ₹3 CRORE\n14)   ₹7 CRORE')
print('\n********************************GAME**********************************')
print('\n--You can type your answer between options "a" "b" "c" "d" \n--You can type 50 for 50:50 lifeline and 75 for 75:25 lifeline\n--You can type quit if you want to quit the game')

def quit(res):
  if(res=='quit'):
    print("\nyou chose to quit the game \nYou have won ",amount[i])
    print('\nTHANK YOU for playing the game')
    exit()

def fifty(res):
  if(no50==0):
      if(res=='50'):
        e=random.choice(wrongans[k])
        index1= wrongans[k].index(e)
        wrongans[k].pop(index1)
        f=random.choice(wrongans[k])
        index2=wrongans[k].index(f)
        wrongans[k].pop(index2)
        print('----------------------------------------------------------------------------------')
        print('\n Here is your question after using your life line:\n\n ',questions[j][0],'\n',wrongans[j][0],'\n',answer[j][1])
        return no50+1
  else:
    print('You have already used this lifeline once')

def seventy(res):
  if(no75==0):
    if(res=='75'):
      e=random.choice(wrongans[k])
      index1= wrongans[k].index(e)
      wrongans[k].pop(index1)
      print('\n Here is your question after using your life line:\n\n ',questions[j][0],'\n',wrongans[j][0],'\n',wrongans[j][1],'\n',answer[j][1])
      return no75+1
  else:
    print('you have alredy used this lifeline')

def nolifeline(res):
  if(res==answer[j][0]):
    print('CORRECT ANSWER')
    print('you have won :',amount[i+1])
  else:
    print("\nYou have chosen the wrong option \nYou have won ",amount[i])
    print('\nTHANK YOU for playing the game')

print('\n***************************** Let the game begin ***********************')
m=0
k=0
i=0
j=0
no50=0
no75=0

for x in range(0,14):
  print('----------------------------------------------------------------------------------')
  print(f'\nHere is your Question {i+1} for {amount[i+1]} :\n\n ',questions[m][0],'\n',questions[m][1],'\n',questions[m][2],'\n',questions[m][3],'\n',questions[m][4])
  res = input("\nInput the chosen option : a  b  c  d\nTo quit type 'quit'\nTo use life line type '50' or '75'\nANS :").lower()
  if(res=='a'or res=='b'or res=='c'or res=='d'):
    nolifeline(res)
  else:
    match res:
      case 'quit':
        quit(res)
      case '50':
        no50=fifty(res)
      case '75':
        no75=seventy(res)
    print('----------------------------------------------------------------------------------')
    ans50=input("input options : 'a' 'b' 'c' 'd' \n")
    if(ans50==answer[j][0]):
      print('CORRECT ANSWER')
      print('you have won :',amount[i+1])
    else:
      print("\nYou have chosen the wrong option \nYou have won ",amount[i])
      print('\nTHANK YOU for playing the game')
  i=i+1
  j=j+1
  k=k+1
  m=m+1 
