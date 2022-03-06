#  Main Program
import cv2
import time
import GestureData as Gd

i=0
LHpt=8
pTime=0
cTime=0
cap=cv2.VideoCapture(0)
x,y = cap.read()
Width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
Height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
RectDim=100
cap.set(3,Width)
cap.set(4,Height)
detector=Gd.handDetector()

mypoints = []
textarray = [" Blue",'Green','  Red','Yellow',' White',' Clear']
colorarray = [(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,255),(255,255,255)]
scale = Width/len(textarray)
color = (255,0,0)

Clear=True

def ChangeColor(i):
        return (colorarray[i][0],colorarray[i][1],colorarray[i][2])

def Clearing(j):
    if (j == len(colorarray)-1):
        return True
    else:
        return False

while True:

        success,img=cap.read()
        Img = img.copy()
        img=detector.findHands(img,False)
        List=detector.findPos(img)

        if len(List)!=0 :
            cv2.circle(img,(int(List[8][1]) ,int(List[8][2])),10,(255,120,0),10)
            if Clear ==True:
                mypoints.clear()
                # print('hi')
        
            if Clear == False:
                mypoints.append([int(List[8][1]) ,int(List[8][2])])
            
            for j in range(len(colorarray)):
                if( int(scale*j)+10 < int(List[8][1]) < int((scale*j)+scale-35) and 40 <int(List[8][2])<80 ) :
                    Clear = Clearing(j)

        if len(mypoints)!=0:
            for i in mypoints:
                cv2.circle(img,(int(i[0]) ,int(i[1])),2,(color),2)
                for j in range(len(colorarray)-1):
                    if( int(scale*j)+10 < int(i[0]) < int((scale*j)+scale-35) and 40 <int(i[1])<80 ) :
                        color = ChangeColor(j)
                        

                

        cTime=time.time()
        FPS=1/(cTime-pTime)
        pTime=cTime

        for i in range(len(textarray)):
            cv2.rectangle(img,(int((scale*i)+scale-20),40),(int(scale*i)+10,75),(colorarray[i][0],colorarray[i][1],colorarray[i][2]),cv2.FILLED)
            cv2.putText(img,(textarray[i]),(int(scale*i)+10,65),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)

        # cv2.putText(img,str(int(FPS)),(10,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),1)
        
        cv2.imshow("Image",img)

        if cv2.waitKey(1) & 0xff == ord('j'):
            break

# //////////////////////////////////////////////////////////////////////////////// Made By Harsh Maurya.......With 💖 
