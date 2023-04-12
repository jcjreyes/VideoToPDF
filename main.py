import sys
import cv2
from energy_computer import EnergyComputer
from arg_parser import ArgumentParser

# Initialization
ec = EnergyComputer()
args = ArgumentParser()
src = args.run(sys.argv[1:])
fileName: str = src.src
path: str = src.output
print("File", fileName, " being processed")

cap = cv2.VideoCapture(fileName)
count: int = 0
frame_num: int = 0
interval_length: float = src.interval
fps: int = cap.get(cv2.CAP_PROP_FPS)
num_frames_per_interval: int = int(interval_length * fps)

# Main Loop
ret, frame = cap.read()
while ret:
    if count % num_frames_per_interval == 0:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Current Frame", frame)
        ec.add(frame)

        if ec.isNew():
            print("NEW!")
            cv2.imwrite(f"{path}/{count}.png", frame)

        # Skips the frames ahead towards to the interval_length
        for i in range(num_frames_per_interval - 1):
            ret, frame = cap.read()
            count += 1

    count += 1

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
