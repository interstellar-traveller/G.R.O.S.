import cv2
import mediapipe as mp
import math
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
drawing_styles = mp.solutions.drawing_styles

scale_access = False

def dis(x1,y1,x2,y2,z1,z2):
  return math.sqrt(((x1-x2)**2+(y1-y2)**2)+(z1-z2)**2)
def changeIn(a,b): # 两个数相差的值
  return a-b
def scale_dis(len,z):
  return len
# For static images:
IMAGE_FILES = []
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
  for idx, file in enumerate(IMAGE_FILES):
    # Read an image, flip it around y-axis for correct handedness output (see
    # above).
    image = cv2.flip(cv2.imread(file), 1)
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print handedness and draw hand landmarks on the image.
    print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
      continue
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()
    for hand_landmarks in results.multi_hand_landmarks:
      print('hand_landmarks:', hand_landmarks)
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
      )
      mp_drawing.draw_landmarks(
          annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
          drawing_styles.get_default_hand_landmark_style(),
          drawing_styles.get_default_hand_connection_style())
    cv2.imwrite(
        '/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.65,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # for id, lm in enumerate(handLms.landmark):
            #     print(id, lm)
            #     # 获取手指关节点
            h, w, c = image.shape #获取图像长宽
            #     cx, cy = int(lm.x*w), int(lm.y*h)
            #     cv2.putText(image, str(int(id)), (cx+10, cy+10), cv2.FONT_HERSHEY_PLAIN,
            #     1, (0, 0, 255), 2)
            z1=handLms.landmark[0].z
            x1=handLms.landmark[0].x*w
            y1=handLms.landmark[0].y*h
            z2=handLms.landmark[12].z
            x2=handLms.landmark[12].x*w
            y2=handLms.landmark[12].y*h
            tai = dis(x1,x2,y1,y2,z1,z2)
            if(math.fabs(changeIn(tai,dis(x1,x2,y1,y2,z1,z2)))>=10):
              print(tai)
              print(z1)
            
            print(tai)
            print(z1)
            # print(tai)
            # print(x1-z1,x2-z2)
            # if(tai>=0.62):
            #       print("全张")
            # elif(tai<=0.54 and tai >= 0.45):
            #       print("半张")
            # elif(tai<=0.32 and tai>=0.25):
            #       print("微握")
            # elif(tai<=0.22):
            #       print("全握")

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
            drawing_styles.get_default_hand_landmark_style(),
            drawing_styles.get_default_hand_connection_style())
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()