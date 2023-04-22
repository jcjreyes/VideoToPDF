from collections import deque
import cv2
import numpy as np


class EnergyComputer:
    def __init__(self):
        self.average_energy = 0
        self.energy_queue = deque(maxlen=5)
        self.energy_queue.extend([0, 0, 0, 0, 0])

    def add(self, image):
        """
        Calculates the energy of an image and adds it to the queue.
        If the queue is full, the oldest value is removed.
        If the energy is more than 350000 different from the current average,
        the value is added 4 more times, preserving the current 'existing' frame
        as the new average_energy value.
        """

        energy = self.__compute_energy(image)
        self.energy_queue.append(energy)
        self.__update_average()

        if self.isNew():
            self.energy_queue.extend([energy] * 4)

    def isNew(self) -> bool:
        """
        Checks if the latest energy value is significantly different from the average.
        Returns True if the difference is more than 350000, False otherwise.
        """
        latest_energy = self.energy_queue[-1]
        return abs(latest_energy - self.average_energy) >= 250000

    def get_energy_queue(self):
        """
        Returns the energy queue.
        """
        return self.energy_queue

    def __compute_energy(self, image):
        """
        Calculates the energy of an image by computing the Canny edge detection
        and summing the resulting frame.
        """
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edge_frame = cv2.Canny(image_gray, 100, 200)
        return np.sum(edge_frame)

    def __update_average(self):
        """
        Calculates the average energy of the queue.
        """
        self.average_energy = sum(self.energy_queue) / len(self.energy_queue)

    def __test__(self):
        print(self.energy_queue)
        print(self.average_energy)
        print(self.isNew())
