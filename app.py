import numpy as np
from flask import Flask, request, render_template
import keras


# Create app object using Flask
app = Flask(__name__)

# Load trained model
model = keras.models.load_model("./models/model.h5")
