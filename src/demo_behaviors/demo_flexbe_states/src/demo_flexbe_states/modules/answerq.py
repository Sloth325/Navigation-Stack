# coding=utf-8
import mic
import simple_speek
import simple_voice

endlist=["再见","拜拜","那没事了","停止"]
actionlist=["去","前往","导航","回"]
placelist=["信息学院","信院","生命学院","物理学院","宿舍","寝室"]
thinglist=["学习","开会","参加活动"]
positivelist=["是的","对","嗯"]
negativelist=["不是","不对","错"]


place=""
action=""
feedback=True

def getans(a,p,curr_state):
    ans="我不明白你在说什么,请在说一遍"
    with open('result.txt', 'rb') as speech_file:
        TEXT = speech_file.read()
        s=TEXT.find('['.encode())
        e=TEXT.find(']'.encode())
        TEXT=TEXT[s+1:e].decode()#TEXT is the input words
        print(TEXT)

    action=a
    place=p
    feedback=True
    # with open("action.txt","w") as act:
    #     action=act.read()
    # with open("place.txt","w") as act:
    #     action=act.read()

    for i in placelist:
        if i in TEXT:
            place=i
            break

    for i in actionlist:
        if i in TEXT:
            action=i
            break

    for i in positivelist:
        if i in TEXT:
            feedback=True
            break

    for i in negativelist:
        if i in TEXT:
            feedback=False
            break

    for i in endlist:
        if i in TEXT:
            ans="好的,再见"
            curr_state="standby"
            place=""
            action=""
            return ans,curr_state,action,place



    if curr_state=="standby":

        if place!="" and action!="":
            ans="您是要"+action+place+"吗？"
            curr_state="checking"
            return ans,curr_state,action,place
        if place=="":
            ans="您想去哪里呢？"
            curr_state="requesting"
            return ans,curr_state,action,place

    if curr_state=="requesting":
        if place!="":
            ans="您是要去"+place+"吗？"
            curr_state="checking"
            return ans,curr_state,action,place
        else:
            ans="您想去哪里呢？"
            curr_state="requesting"
            return ans,curr_state,action,place

    if curr_state=="checking":
        if feedback==True:
            ans="受到，路径规划成功，please follow me"
            place=""
            action=""
            curr_state="standby"
            return ans,curr_state,action,place
        else:
            ans="好的，那您想去哪呢？"
            curr_state="standby"
            place=""
            action=""
            return ans,curr_state,action,place


    

    return ans,curr_state,action,place   


