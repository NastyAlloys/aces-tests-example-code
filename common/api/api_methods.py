import random
from common.settings import GIF_IDS


class ApiMethods:
    def create_ace_with_gif(self, api_service):
        random_gif_id = random.choice(GIF_IDS)
        uploaded_giphy = api_service.upload_giphy(random_gif_id)

        ace_data = {
            "is_public": True,
            "content_id_ordering": [uploaded_giphy["id"]],
            "content_attributes": [],
            "recipient_ids": [],
            "image_ids": [],
            "video_ids": [],
            "link_ids": [],
            "file_ids": [uploaded_giphy["id"]]
        }

        new_ace = api_service.create_ace(ace_data)
        new_ace_id = str(new_ace["id"]).upper()

        return new_ace_id

    def create_ace_with_gif_as_mutual(self, api_service, api_service_as_mutual):
        user_profile = api_service.get_user_profile()

        random_gif_id = random.choice(GIF_IDS)
        uploaded_giphy = api_service_as_mutual.upload_giphy(random_gif_id)

        ace_data = {
            "is_public": False,
            "content_id_ordering": [uploaded_giphy["id"]],
            "content_attributes": [],
            "recipient_ids": [user_profile["id"]],
            "image_ids": [],
            "video_ids": [],
            "link_ids": [],
            "file_ids": [uploaded_giphy["id"]]
        }

        new_ace = api_service_as_mutual.create_ace(ace_data)
        new_ace_id = str(new_ace["id"]).upper()

        return new_ace_id

    def create_flip_with_gif(self, api_service, ace_id):
        random_gif_id = random.choice(GIF_IDS)
        uploaded_giphy = api_service.upload_giphy(random_gif_id)

        flip_data = {
            "ace_id": ace_id,
            "annotation_data": {
                "gifs": [{
                    "gif_id": uploaded_giphy["id"],
                    "position_x": 100,
                    "position_y": 100,
                    "position_z": 100,
                    "rotate": 0.5,
                    "scale": 0.5
                }]
            }
        }

        new_flip = api_service.create_flip(flip_data)
        new_flip_id = str(new_flip["id"]).upper()

        return new_flip_id
