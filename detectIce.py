from tensorflow.keras.models import load_model
import cv2
import pymysql
from time import sleep
import sys
import datetime

try:
    conn = mariadb.connect(host='host', user = 'id', password='password@@', db='blackice', port=13307) 
except:
    print("Failed to Connect")
    sys.exit(1)    

camera = cv2.VideoCapture(0) # camera load
# value = ["DRY", "WATER", "ICE"]
empty = []

#아래는 데이터 입력값
nowDate = 0
longitude = 0
latitute = 0
state = "dry"
###############################

last_value = 0 # 이전값 과 달라졌을때만 DB에 insert

cur = conn.cursor() # 커서 세팅


model = load_model('/home/pi/Desktop/CNNmodel') #model load



while True:
    ret,frame = camera.read()
    cv2.waitKey(30) 
    dst = cv2.resize(frame, dsize=(150, 150))
    dst = dst.reshape(-1, 150, 150, 3)
    y_pred = model.predict(dst)

    print(y_pred) # list 내부의 확률로 출력 예상
    

    empty.append(y_pred[0][0], y_pred[0][1])
    idx = empty.index(max(empty)) # 현재 결과값 출력
    
    nowDate = str(datetime.datetime.now())
    longitude = 37.66666 # 일단 임의값
    latitute = 126.7777 #일단 임의값

    if last_value == idx: # 데이터가 같으면 이전으로 돌아가라.
        continue

    if idx == 1:
        print("water")
        state = "water"

    elif idx == 0:
        print("dry")    
        state = "dry"
    elif idx == 2 :
        print("ice")
        state = "ice"

    last_value = idx    

    SQL = f"insert into blackice_list(date,latitude, longitude, ice_type) values(?,?,?,?)"
    cur.execute(SQL,(nowDate,latitute,longitude,state))
    conn.commit()



    sleep(0.5)