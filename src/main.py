import sys
import os
import cv2
from .energy_computer import EnergyComputer
from .arg_parser import ArgumentParser


def get_args():
    args = ArgumentParser().run(sys.argv[1:])
    return args.src, args.output, args.interval


def main():
    fileName, output_path, interval_length = get_args()

    cap = cv2.VideoCapture(fileName)
    fps = cap.get(cv2.CAP_PROP_FPS)
    num_frames_per_interval = int(interval_length * fps)

    energy_computer = EnergyComputer()
    count = 0
    frame_num = 0

    if os.path.exists(output_path):
        print("Folder found.")
    else:
        os.makedirs(output_path)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if count % num_frames_per_interval == 0:
            cv2.imshow("Video", frame)
            energy_computer.add(frame)

            if energy_computer.isNew():
                print("New frame detected.")
                cv2.imwrite(f"{output_path}/{frame_num:04d}.png", frame)
                frame_num += 1

            for _ in range(num_frames_per_interval - 1):
                ret, frame = cap.read()
                count += 1

        count += 1

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def convert_to_pdf():
    _, folder, _ = get_args()


if __name__ == "__main__":
    main()
