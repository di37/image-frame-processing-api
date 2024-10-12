import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

IMAGE_FRAMES_CSV_PATH = os.getenv("IMAGE_FRAMES_CSV_PATH", "data/raw/image_data.csv")
DATABASE_PATH = os.getenv("DATABASE_PATH", "data/processed/image_data.db")

MIN_PIXEL = 0
MAX_PIXEL = 255
HEIGHT = 1  # The reason it was set to 1 is that we were treating each row of the CSV as a single line of pixels, essentially creating a 1-pixel high image.
WIDTH = 200
NEW_WIDTH = 150
IMAGE_FORMAT = "PNG"
