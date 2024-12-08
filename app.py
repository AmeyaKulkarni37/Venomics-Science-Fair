import numpy as np
from flask import Flask, request, render_template
import keras
from keras.utils import pad_sequences



# Create app object using Flask
app = Flask(__name__)

# Load trained model
model = keras.models.load_model("./models/model.h5")

@app.route("/")
def home():
    return render_template("index.html")


codes = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
         'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']


def create_dict(codes):
  char_dict = {}
  for index, val in enumerate(codes):
    char_dict[val] = index+1

  return char_dict

char_dict = create_dict(codes)

def integer_encoding(data):
  encode_list = []
  for row in data['Sequence'].values:
    row_encode = []
    for code in row:
      row_encode.append(char_dict.get(code, 0))
    encode_list.append(np.array(row_encode))

  return encode_list

def test_encode(sequ):
  ret_list = []
  encoded_list= []
  for code in sequ:
    encoded_list.append(char_dict.get(code, 0))
  ret_list.append(encoded_list)
  ret_list = pad_sequences(ret_list, maxlen=600, padding='post', truncating='post')
  return ret_list


@app.route("/predict", methods=["POST"])
def predict():
    classes = np.array(['GO:0090729', 'GO:0005179', 'GO:0016829',
       'GO:0046872', 'GO:0008081', 'GO:0004867', 'GO:0099106', 'GO:0015459',
       'GO:0004252', 'GO:0005246', 'GO:0004623', 'GO:0005509', 'GO:0008200',
       'GO:0017080', 'GO:0019834', 'GO:0008270', 'GO:0030550', 'GO:0004222',
       'GO:0052740', 'GO:0052739', 'GO:0008970', 'GO:0050025', 'GO:0050029',
       'GO:0106329', 'GO:0008191', 'GO:0004620', 'GO:0008233', 'GO:0016504',
       'GO:0060422', 'GO:0000166', 'GO:0106411', 'GO:0000287', 'GO:0008237',
       'GO:0005102', 'GO:0005216', 'GO:0008201', 'GO:0008236', 'GO:0008289',
       'GO:0019870', 'GO:0019871', 'GO:0004465', 'GO:0016491', 'GO:0042802',
       'GO:0047498', 'GO:0048018', 'GO:0001515', 'GO:0001716', 'GO:0042803',
       'GO:0003677', 'GO:0050660', 'GO:0003990', 'GO:0003993', 'GO:0004175',
       'GO:0004177', 'GO:0004415', 'GO:0008239', 'GO:0004556', 'GO:0004860',
       'GO:0004866', 'GO:0004869', 'GO:0005154', 'GO:0005184', 'GO:0005185',
       'GO:0005507', 'GO:0005516', 'GO:0005520', 'GO:0005534', 'GO:0030395',
       'GO:0033296', 'GO:0008061', 'GO:0008083', 'GO:0016603', 'GO:0016787',
       'GO:0019855', 'GO:0003676', 'GO:0016853', 'GO:0017081', 'GO:0044325',
       'GO:0030246', 'GO:0030414', 'GO:0033906', 'GO:0043262', 'GO:0048019',
       'GO:0070320', 'GO:0080030', 'GO:0140628'])
    

    input = request.form["Input Sequence"]
    encoded = test_encode(input)
    prediction = model.predict(encoded)
    indices = np.argsort(prediction[0])[:-11:-1]
    top_classes = classes[indices]
    top_probs = prediction[0][indices]


    

    out = [
        {"class": top_classes[i], "probability": f"{top_probs[i]:.3f}"}
        for i in range(10)
    ]

    return render_template("index.html", predictions=out)


if __name__ == "__main__":
  app.run()