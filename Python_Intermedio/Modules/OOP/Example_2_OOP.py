class PhotographyCamera:
    photograpies = []
    def __init__(self, storage_size_in_mb ):
        self.max_photographies = storage_size_in_mb / 10
    def take_photo(self, photography):
        if len(self.photograpies) >= self.max_photographies:
            print("My storage is full")
            return

        self.photograpies.append(photography)
kodak_camera = PhotographyCamera(20)
kodak_camera.take_photo("my car")
kodak_camera.take_photo("my house")
kodak_camera.take_photo("my dog")
print(kodak_camera.photograpies)