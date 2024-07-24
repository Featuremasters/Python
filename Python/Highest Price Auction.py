print("Welcome to the HIGHEST PRICE AUCTION")
print('''                                     
                               ^)))(])^                                    
                                +]])<^)[]<-                                
                               ..:~^([]]]]]]                               
                              ......-~*)[]](                               
                             ......------                                  
                              ....------*                                  
                         : ~=....------*).                                 
                        <))((]]*------*][](<=                              
                         []())(]][<=-     ~[]])^                           
                            ([]]](^:          )[]()+                       
                               >}[]]>            >[]](<.                   
                                                    +[]]((+                
                                                       .][]((<             
                 =][[[[[[[[[>]{{{{{{{{{}.                  >]]]=(^         
               <))))))))))))(]]]]]]]]]]]]](                   *]]]((>      
               (]]]]]]]]]]]][}}}}}}}}}}}}}}~                     =(][)     
                                                ''')
def loop():
    more=input("Are there any bidders, Type 'yes' or 'No'\n").lower()
    if more=="yes":
        add(bidders)
    elif more=="no":
        align=0
        for i in range(len(bidders)):
            value=bidders[i]["Price"]
            if value>align:
                align=value
                winner=bidders[i]["Name"]
        print(f"The highest bidders is value is {align} and the bidder is {winner}")       
    else:
        print("Enter the right input")
        c=False
        while not c:
            loop()
        
def add(bidders):
    name=input("What is your Name\n")
    price=int(input("What is your bid\n"))
    a={}
    a["Name"]=name
    a["Price"]=price
    bidders.append(a)
    loop()
bidders=[]  
add(bidders)