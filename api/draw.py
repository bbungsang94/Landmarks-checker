import cv2


def draw_points(image, coordinates):
    # x, y 하나씩인 경우와 튜플인 경우가 있음
    if isinstance(coordinates[0], float):
        if len(coordinates) % 2 != 0:
            return None
        image = Drawer.draw_list(image, coordinates)
    else:
        image = Drawer.draw_tuple(image, coordinates)
    return image

class Drawer:
    @staticmethod
    def draw_list(image, coordinates):
        number = 0
        for index in range(0, len(coordinates), 2):
            x = coordinates[index]
            y = coordinates[index + 1]
            image = cv2.circle(image, (int(x), int(y)), 3, (0, 255, 0), 2)
            image = cv2.putText(image, '%02d' % number, (int(x) - 20, int(y) - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 1, cv2.LINE_AA)
            number += 1
        return image

    @staticmethod
    def draw_tuple(image, coordinates):
        for number, coordinate in enumerate(coordinates):
            image = cv2.circle(image, (coordinate[0], coordinate[1]), 3, (0, 255, 0), 2)
            image = cv2.putText(image, str(number), (coordinate[0] + 10, coordinate[1]),
                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 1, cv2.LINE_AA)
        return image