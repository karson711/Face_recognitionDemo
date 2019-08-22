
import sys
import face_recognition  #人脸识别库  需要先安装pip cmake dlib
import cv2

#读取图像
face_image = face_recognition.load_image_file(r'6.png')
#给定一张图片 返回图像每个面128维的人脸编码
face_encodings = face_recognition.face_encodings(face_image)
#每个人脸的面部特征位置
face_locations = face_recognition.face_locations(face_image)
#判断图像中的人数
n = len(face_encodings)
print(n)

if n > 2:
    print('3')
    sys.exit()
try:
    face1 = face_encodings[0]
    face2 = face_encodings[1]
except:
    print('2')
    sys.exit()

#比较脸部的编码是否匹配
results = face_recognition.compare_faces([face1],face2,tolerance=0.5)
print(results)

if results == [True]:
    print('1')
    name = 'YES'
else:
    print('0')
    name = 'NO'

#绘图
for i in range(len(face_encodings)):
    face_encoding = face_encodings[(i-1)]
    face_location = face_locations[(i-1)]
    print(face_location)
    top,right,bottom,left = face_location
    #画框            图像              坐标                 颜色    粗细
    cv2.rectangle(face_image,(left,top),(right,bottom),(0,255,0),2)
    # 放上文字 putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None) img： 图像  text：要输出的文本 org： 文字的起点坐标fontFace： 字体 fontScale： 字体大小  color： 字体颜色  thickness： 字图加粗#
    cv2.putText(face_image,name,(left-10,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)

#颜色
face_image_rgb = cv2.cvtColor(face_image,cv2.COLOR_BGR2RGB)

#展示图像
cv2.imshow('Output',face_image_rgb)

#保存图像
cv2.imwrite(r'/Users/anfa/Desktop/result.jpg',face_image_rgb,[int(cv2.IMWRITE_JPEG_QUALITY),100])
#关闭
cv2.waitKey(0)