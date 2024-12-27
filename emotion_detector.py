import cv2
from deepface import DeepFace

def detect_emotion():
    # Open webcam
    cap = cv2.VideoCapture(0)
    print("Press 'q' to capture the emotion and exit.")
    
    emotion = None
    while True:
        ret, frame = cap.read()
        cv2.imshow("Webcam - Emotion Detection", frame)
        
        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            try:
                # Analyze emotion
                analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                emotion = analysis['dominant_emotion']
            except Exception as e:
                print("Error detecting emotion:", e)
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return emotion
