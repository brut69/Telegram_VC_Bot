HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["7703315"])
    API_HASH = environ["43118491ea08de184cbbcd11a93398ec"]
    SESSION_STRING = environ[
        "BQAoVlgvn-HVXQM4zGwuJl_BsId67C_HhghZyTEnJpn_aWjYYrWaRD0OlQlk1JGY29R7qPvuuANVvUDxErMjT1Ii9vYYV4rUVJE2nUVCr9odxozgnTXfr0MEZ7-DyjOGstciauZHJ5xdpck_Pxo8NBswzBedChcLMQVp5HY4R8-73Tqgq4HaZ5Xl_1ESV7oKyNQRek45QsDOapLvfFjAYO7ee2y8XzNHgmRYY5Nm_CawbYHm8MqoYLNhUhhxqaG-MzW8NQrGeyiLsG9zcin26VM5RlsgNzEQ_k4nfN8YFNcX30iDppmknWvOKHxnk2nm-8b7R0ZHPXO9YkA947CqyYzhc_w-0wA"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 7703315
    API_HASH = "43118491ea08de184cbbcd11a93398ec"
    ARQ_API_KEY = "AUDEEE-WKVNES-UGXHIX-QFDHIU-ARQ"
    CHAT_ID = -1001356822547
    DEFAULT_SERVICE = "youtube"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech"
