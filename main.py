import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)


mpHand = mp.solutions.hands

hands = mpHand.Hands()

mpDraw = mp.solutions.drawing_utils

tipIds = [4,8,12,16,20] #parmakların uç noktalarını belirttik

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    
    TotalFingers = 0
   
    if results.multi_hand_landmarks:
        # ÖNEMLİ: Her bir el için ayrı işlem yapmalıyız
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms , mpHand.HAND_CONNECTIONS)
            
            LmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                
                cx, cy = int(lm.x*w), int(lm.y*h)
                
                LmList.append([id, cx, cy])
                # her bir eklemin idsini ve konumunu liste içine attık.
                # böylece her bir eklemin anlık konumuna erişebilmiş olduk
                
            if len(LmList) != 0:
                fingers = []
                
                # SOL EL İÇİN 
                # Baş parmağımızın uç noktası, serçe parmağımızın kökünün solunda 
                # kalıyorsa bu sol elimizdir tespitini yaptık. 
                # otomatik aynalama olduğu için küçüktür büyüktür işaretleri ters oldu
                # yani kamera ayna görüntüsü verdiği için X ekseni kontrolleri ters mantıkla kuruldu.
                
                if LmList[tipIds[0]][1] < LmList[tipIds[4] -3][1]:
                # Baş parmak için 
                
                    if LmList[tipIds[0]][1] < LmList[tipIds[0] - 1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                        
                    # 4 parmak için
                    
                    for id in range (1,5):
                        
                        if LmList[tipIds[id]][2] < LmList[tipIds[id]-2][2]:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                  
                   
                
                else: #SAĞ EL İÇİN
                    
                # Baş parmak için 
                    if LmList[tipIds[0]][1] > LmList[tipIds[0] - 1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                        
                    # 4 parmak için
                    
                    for id in range (1,5):
                        
                        if LmList[tipIds[id]][2] < LmList[tipIds[id]-2][2]:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                  
                TotalFingers += fingers.count(1)
                
    cv2.putText(img , str(TotalFingers), (30,125), cv2.FONT_HERSHEY_PLAIN , 10 , (255,0,0),8)
            
                
    
    cv2.imshow("img" , img)
    cv2.waitKey(1)
    
    
    
    
    # BİZ DEDİK Kİ EĞER BİR PARMAĞIN UÇ NOKTASINDAKİ EKLEM, KENDİNDEN 2 
    # ALTTAKİ EKLEMİN KOORDİNAT OLARAK ALTINA GELİRSE. BİZ BU PARMAĞI KIRMIŞIZ
    # DEMEKTİR. BUNA GÖRE ALGORİTMAMIZI YAZACAĞIZ. 
    # DAHA İYİ ANLAYABİLMEK İÇİN UÇ NOKTAYI VE İKİ ALTINI İŞARETLEDİK VE
    # DENEYEREK DOĞRU OLDUĞUNU GÖRDÜK
    
    
    # if id == 8 :  #İŞARET PARMAĞI UÇ NOKTASI
    #     cv2.circle(img,(cx,cy),9,(255,0,0),cv2.FILLED)
        
    
    
    # if id == 6:   #İŞARET PARMAĞI UÇ NOKTASININ İKİ ALTINDAKİ EKLEM
    #     cv2.circle(img,(cx,cy),9,(0,0,255),cv2.FILLED)
    
    
    
    # BU KODU  LmList.append([id, cx, cy]) ALTINA YAPIŞTIRARAK DENEYEBİLİRİZ.