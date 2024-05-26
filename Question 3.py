import json
q = { }
scr = 0
numb=1
m = open("questions.txt",'r')
q = json.load(m)
m.close()
print("Enter t , f")
name = input("Enter your name: ")
for x in q :
    print("Question",numb,": ", x)
    answer = input("The answer is ")
    if answer == q[x]:
        scr = scr + 1
    numb = numb + 1
result={name:scr}
y = open("score.txt",'w')
result = json.dump(result,y)
y.close()