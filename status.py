from pypresence import Presence
import time

# -------------------------------
# Fill your informations
# -------------------------------

CLIENT_ID = ""                            # Application id from Discord Developer Portal
DETAILS = ""                              # Big Title
STATE = ""                                # State title
LARGE_IMAGE_KEY = ""                      # Key name of the Art asset on your Rich Presence 
LARGE_TEXT = ""                           # Text on your image
SMALL_IMAGE_KEY = ""                      # Little Image Key (optional)
SMALL_TEXT = ""                           # Little Image Text (optional)
START_TIME = int(time.time())             


rpc = Presence(CLIENT_ID)
rpc.connect()

try:
    rpc.update(
        details=DETAILS,
        state=STATE,
        start=START_TIME,
        large_image=LARGE_IMAGE_KEY,
        large_text=LARGE_TEXT,
        small_image=SMALL_IMAGE_KEY if SMALL_IMAGE_KEY else None,
        small_text=SMALL_TEXT if SMALL_TEXT else None
    )
    print("Status set, Control+C for exit.")
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    print("\nStatus cleared.")
    try:
        rpc.clear()
    except:
        pass
    rpc.close()