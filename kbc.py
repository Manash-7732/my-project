qus=["Which one of the following river flows between Vindhyan and Satpura ranges?","The Central Rice Research Station is situated in?" , " Who among the following wrote Sanskrit grammar?" , "Which among the following headstreams meets the Ganges in last?" , "The metal whose salts are sensitive to light is?" ]

firstoption=["a.Narmada","a.Chennai","a.Kalidasa" ,"a.Alaknanda","a.Zinc"]
secondoption=["b.Krishna","b.kattak","b.charak","b.Pindar","b.Silver"]
thirdoption=["c.son","c.bangalore","c.pinani","c.mandakani","c.copper"]
fourthoption=["d.netravati","d.quilon","d.aryabhatt","d.bhagirathi","d.aluminium"]

answerkeys=["a","b","c","d","b"]

levels=[1000,2000,3000.4000,50000]

i=0

correct=0

x=0

while(i<len(qus)):
    print(qus[i])
    print(firstoption[i])
    print(secondoption[i])
    print(thirdoption[i])
    print(fourthoption[i])
    
    ans=input("Enter your answer: ")
    
    if ans == answerkeys[i]:
        print("Correct Answer")
        correct=1
    else:
        print("Wrong Answer")
        correct=0
        break

    if(correct==1):
       x=x+levels[i]
    i=i+1   




   

print("the score is" + str(x))
      

