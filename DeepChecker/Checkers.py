

import pickle
import os
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle
from keras.models import Model, Sequential
import re
import tensorflow as tf
from keras.layers import Dense, LSTM, Flatten, Embedding, Dropout , Activation, GRU, Flatten, Input, Bidirectional, GlobalMaxPool1D, Convolution1D, TimeDistributed, Bidirectional
from keras.layers.embeddings import Embedding

this_dir, this_filename = os.path.split(__file__)


def build_model(embedsize):
    model = Sequential()
    model.add(Embedding(15000, embedsize))
    model.add(Bidirectional(LSTM(64, return_sequences = True)))
    model.add(Bidirectional(LSTM(32, return_sequences = True)))
    model.add(GlobalMaxPool1D())
    model.add(Dense(1, activation="sigmoid"))
    return model

def check_de(text):
    tokenizerpath = os.path.join(this_dir, "tokenizers", "tokenizer_deda.pickle")
    weigthpath = os.path.join(this_dir, "weights", "Model_deda.h5")
    model = build_model(128)
    with open(tokenizerpath, 'rb') as handle:
        turkish_tokenizer = pickle.load(handle)
    model.load_weights(weigthpath)
    tokens = turkish_tokenizer.texts_to_sequences([text])
    tokens_pad = pad_sequences(tokens, maxlen=7)
    res = model.predict(tokens_pad)
    
    return (res[0][0])

def correct_de(text):
    arr = text.split()
    for i in range(len(arr)):
        tmparr = text.split()
        last2 = arr[i][-2:]
        if last2 == "de" or last2 == "da":
            if len(arr[i]) == 2:
                tmparr[i] = "x"
                changed = ' '.join(tmparr[0:])
                if check_de(changed) > 0.5:
                    if last2 == "de":
                        arr[i-1] = arr[i-1]+"de"
                        arr[i] = ""
                    elif last2 == "da":
                        arr[i-1] = arr[i-1]+"da"
                        arr[i] = ""
            elif len(arr[i])>2:
                rest = arr[i][:-2]
                tmparr[i] = rest + " x"
                changed = ' '.join(tmparr[0:])
                if check_de(changed) < 0.5:
                     if last2 == "de":
                        arr[i] = arr[i][:-2] + " de"
                     elif last2 == "da":
                        arr[i] = arr[i][:-2] + " da"
    
    result = ' '.join(arr[0:])
    return result


#print(correct_de("böyle koşullar da çalışmakda çok sıkıcı 99"))



def check_ki(text):
    tokenizerpath = os.path.join(this_dir, "tokenizers", "tokenizer_ki.pickle")
    weigthpath = os.path.join(this_dir, "weights", "Model_ki.h5")
    model = build_model(128)
    with open(tokenizerpath, 'rb') as handle:
        turkish_tokenizer = pickle.load(handle)
    model.load_weights(weigthpath)
    tokens = turkish_tokenizer.texts_to_sequences([text])
    tokens_pad = pad_sequences(tokens, maxlen=7)
    res = model.predict(tokens_pad)
    
    return (res[0][0])

def correct_ki(text):
    arr = text.split()
    for i in range(len(arr)):
        tmparr = text.split()
        last2 = arr[i][-2:]
        if last2 == "ki":
            if len(arr[i]) == 2:
                tmparr[i] = "x"
                changed = ' '.join(tmparr[0:])
                if check_ki(changed) > 0.5:
                    arr[i-1] = arr[i-1]+"ki"
                    arr[i] = ""

            elif len(arr[i])>2:
                rest = arr[i][:-2]
                tmparr[i] = rest + " x"
                changed = ' '.join(tmparr[0:])
                if check_ki(changed) < 0.5:
                    arr[i] = arr[i][:-2] + " ki"

    result = ' '.join(arr[0:])
    return result


def check_mi(text):
    tokenizerpath = os.path.join(this_dir, "tokenizers", "tokenizer_mi.pickle")
    weigthpath = os.path.join(this_dir, "weights", "Model_mi.h5")
    model = build_model(128)
    with open(tokenizerpath, 'rb') as handle:
        turkish_tokenizer = pickle.load(handle)
    model.load_weights(weigthpath)
    tokens = turkish_tokenizer.texts_to_sequences([text])
    tokens_pad = pad_sequences(tokens, maxlen=7)
    res = model.predict(tokens_pad)
    
    return (res[0][0])

def correct_mi(text):
    arr = text.split()
    for i in range(len(arr)):
        tmparr = text.split()
        if 'mi' in arr[i]:
            if arr[i].startswith("mi"):
                tmparr[i] = "x"
                changed = ' '.join(tmparr[0:])
                if check_mi(changed) > 0.5:
                    arr[i-1] = arr[i-1] + arr[i]
                    arr[i] = ""
            else:
                tmparr[i] = re.sub(r'mi.*', " x", tmparr[i])
                changed = ' '.join(tmparr[0:])
                if check_mi(changed) < 0.5:
                    arr[i] = arr[i].replace( "mi", " mi", 1)
        elif 'mı' in arr[i]:
            if arr[i].startswith("mı"):
                tmparr[i] = "x"
                changed = ' '.join(tmparr[0:])
                if check_mi(changed) > 0.5:
                    arr[i-1] = arr[i-1] + arr[i]
                    arr[i] = ""
            else:
                tmparr[i] = re.sub(r'mı.*', " x", tmparr[i])
                changed = ' '.join(tmparr[0:])
                if check_mi(changed) < 0.5:
                    arr[i] = arr[i].replace( "mı", " mı", 1)
        elif 'mu' in arr[i]:
            if arr[i].startswith("mu"):
                tmparr[i] = "x"
                changed = ' '.join(tmparr[0:])
                if check_mi(changed) > 0.5:
                    arr[i-1] = arr[i-1] + arr[i]
                    arr[i] = ""
            else:
                tmparr[i] = re.sub(r'mu.*', " x", tmparr[i])
                changed = ' '.join(tmparr[0:])
                if check_mi(changed) < 0.5:
                    arr[i] = arr[i].replace( "mu", " mu", 1)                   
        elif 'mü' in arr[i]:
            if arr[i].startswith("mü"):
                tmparr[i] = "x"
                changed = ' '.join(tmparr[0:])
                if check_mi(changed) > 0.5:
                    arr[i-1] = arr[i-1] + arr[i]
                    arr[i] = ""
            else:
                tmparr[i] = re.sub(r'mü.*', " x", tmparr[i])
                changed = ' '.join(tmparr[0:])
                if check_mi(changed) < 0.5:
                    arr[i] = arr[i].replace( "mü", " mü", 1)

    result = ' '.join(arr[0:])
    return result



#print(correct_mi("müdür müdür müdür"))
print(correct_mi("gülüyormusun"))
#print(check_mi("müdür"))