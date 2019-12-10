from transitions.extensions import GraphMachine
import random
from utils import send_text_message
def maysong():
    m=man
    t=thing
    maysong0="中方對此嚴正聲明：man任何企圖干預中國內政、阻礙中國發展的把戲都不會得逞，到頭來只會是枉費心機一場空。對於man的錯誤做法，中方必將採取有力的措施堅決予以反制，堅定地維護自身主權、安全、發展利益。"
    maysong1="man如果thing不僅將損害中方利益，損害中國和man關係，也將嚴重損害man自身的利益。還是我們經常說的那句話，請man不要高估自己的造謠能力，也不要低估別人的判斷能力。謊言重複一千遍，依然還是謊言。中方正告man，任何企圖破壞中國社會繁榮穩定、阻礙中國發展的圖謀都不會得逞，到頭來只會搬起石頭砸自己的腳。"
    maysong2="我們敦促man懸崖勒馬，否則必將自食惡果，勿謂言之不預也！man自己不願意投入，卻千方百計干擾破壞中國和其他國家開展合作。如果man一意孤行，繼續thing，中方必將採取有力措施予以堅決反制。中國一向秉持和平共處五項原則處理國與國關係，歷來堅定奉行不干涉內政原則，主張各國根據自身國情選擇發展道路。"
    maysong3="man罔顧事實、顛倒黑白，公然thing，性質極其惡劣，用心十分險惡，其根本目的是干涉中國內政，破壞中華民族實現偉大復興的歷史進程。在國際社會大家庭裡,中國始終維護和平,促進發展,堅守道義,同各國攜手構建人類命運共同體。man卻損人利己,唯我獨尊,背信棄義,在世界上大搞順我者昌,逆我者亡。我們敦促man在中國問題上要謹言慎行，不要再發出錯誤信號，不要再挑撥慫恿，不要再幹涉中國內政。中國政府和中國人民堅決反對manthing的行為，中方已就此向man提出嚴正交涉和強烈抗議。"
    #re[]=[maysong0,maysong1,maysong2,maysong3]
    x=random.randrange(0,4)
#     send_text_message(reply_token, maysong0)
    if(x==0):
        k=maysong0
        k=k.replace("man",m)
        k=k.replace("thing",t)
        return k
    elif(x==1):
        k=maysong1
        k=k.replace("man",m)
        k=k.replace("thing",t)
        return k
    elif(x==2):
        k=maysong2
        k=k.replace("man",m)
        k=k.replace("thing",t)
        return k
    else:
        k=maysong3
        k=k.replace("man",m)
        k=k.replace("thing",t)
        return k##12
    
def gettext(k):
    k1=k.find("採取")
    k2=k.find("有何回應")
    global man
    global thing
    man=k[3:k1]
    thing=k[k1+2:k2]
    return
    
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        
    def is_going_to_state1(self, event):
        text = event.message.text#，中方對man採取thing有何回應？
        
        return text.lower() == "ok"

    def is_going_to_user(self, event):
        text = event.message.text
        return text.lower() == "user"

    def is_going_to_state2(self, event):
        text = event.message.text
        k1="中方對"
        k3="採取"
        k2="有何回應"
        if(text.find(k1)!=-1 and text.find(k2)!=-1 and text.find(k3)!=-1):
            gettext(text)
            return True
        return False
        #return text.lower() == "go to state2"
    
    def on_enter_user(self, event):
        print("I'm entering user")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger user")
        
    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "請各方開始提問")
        #self.go_back()

#     def on_exit_state1(self):
#         print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        tex=maysong()
        send_text_message(reply_token, tex)
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
