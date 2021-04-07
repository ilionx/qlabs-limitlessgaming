from Camera.camera import Camera, to_hsv, to_jpg, create_mask


def hsv_camera_feed(settings, camera: Camera = None):
    if camera is None:
        camera = Camera()
    while True:
        frame = camera.read()
        hsv = to_hsv(frame)
        lower_bound = [settings[0]["hueLow"],
                       settings[0]["saturationLow"], settings[0]["valueLow"]]
        upper_bound = [settings[0]["hueHigh"],
                       settings[0]["saturationHigh"], settings[0]["valueHigh"]]
        fourground_mask = create_mask(hsv, lower_bound, upper_bound)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'
               + to_jpg(fourground_mask)
               + b'\r\n\r\n')
