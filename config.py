import os



class Config(object):
      BOT_TOKEN = os.environ.get("8400875138:AAE2zrn4ovvwAj98NPbuXALsPm3rSiRtRIk", "")
      API_ID = int(os.environ.get("25439876"))
      API_HASH = os.environ.get("ae454c231329a1c7e3af30f552a29dc2")
      CAPTION_TEXT = os.environ.get("hello this is encrypted", "")
      CAPTION_POSITION = os.environ.get("BOTTOM", "nil")
      ADMIN_USERNAME = os.environ.get("encryptedxyz", "AvishkarPatil")
