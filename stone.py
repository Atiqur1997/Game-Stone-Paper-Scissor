import random
print("well come")
i=1
while i==1:
    a=random.randrange(1,3)

    round=int(input("round"))
 
    r=a
    countp=0
    countr=0
    while(round>0):
        no=int(input('enter 1 for stone 2 for paper 3 for scissor'))
    
        if (r==1 and no==1)or(r==2 and no==2)or(r==3 and no==3):
            countp+=1
            countr+=1
            
        elif (r==1 and no==2) or (r==2 and no==3) or (r==3 and no==1):
                countp+=1
                
        else:
            countr+=1
        round-=1
        
    if (countp>countr):
        print("you win")
    elif (countp==countr):
        print("equal")
    else:
        print("better luck for next time")
        
    print("your score is %d and score of computer is %d"%(countp,countr))
        
  
    i=int(input("press 1 to play more and press 0 to exit"))
               
    
        
        
        
        
        
        
     
        
        


    
        
    

 
    
    
        
            
            
            
            
            
            
        

        