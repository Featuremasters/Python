from Data import question_data,logo
class Question:
    def __init__(self,qtext,answer):
       self.questions=qtext
       self.answer=answer
class Brain:
    def  __init__(self,qlist):
        self.questionnumber=0
        self.question_list=qlist
        self.score=0
    def list(self):  
        current=self.question_list[self.questionnumber]
        self.questionnumber+=1
        er=True
        while er:
            ans=input(f"Q.{self.questionnumber}: {current.questions}(True or False): ").lower() 
            qans=current.answer
            if ans=="true" or ans=="false":
                self.checkanswer(ans,qans)
                er=False
            else:
                print("Enter the Right Input(True or False)")
    def loop(self):
        if self.questionnumber<len(self.question_list):
                return True
        print("You are done with the quiz")  
        print(F"Final score is{self.score}")
    def checkanswer(self,ans,qans):
        if ans.lower()==qans.lower():
            print("you are Right")
            self.score+=1
        else:
            print("You are Wrong")
        print(F"Your score{self.score}/{self.questionnumber}")
        print("\n")
                    
questionbank=[]    
for i in range(len(question_data)):
   q=question_data[i]["question"]
   a=question_data[i]["correct_answer"]
   n=Question(q,a)
   questionbank.append(n)
   
quiz=Brain(questionbank)
print(logo)
quiz.list()
while quiz.loop():
    quiz.list()


        
