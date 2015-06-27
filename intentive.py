import csv
import time
import numpy as np
import random
import sys

from intentive.model.tools import shuffle, minibatch, contextwin
from intentive.model.elman_rnn import ElmanRNN


def preprocess_dataset(dataset_path='corpora/tasks.csv'):
    text = []
    identifiers = []

    with open(dataset_path, 'r') as f:
        data_iter = csv.reader(f)
        tokens = set()
        for i in data_iter:
            text.append(i[0])
            row = []
            for l in i[2:]:
                row.append(l)
            identifiers.append(row)
            for item in i:
                for t in item.split():
                    tokens.add(t)

    tokens = list(tokens)
    keys = range(0, len(tokens))
    token2idx = dict(zip(tokens, keys))
    idx2token = dict(zip(keys, tokens))

    train_x = []
    for t in text:
        train_x.append(np.asarray([token2idx[k] for k in t.split()]))
    train_y = []
    for i in identifiers:
        train_y.append(np.asarray([token2idx[l] for l in i]))

    return train_x, train_y, token2idx, idx2token


def train():
    s = {'lr': 0.0627142536696559,
         'verbose': True,
        'decay': False, # decay on the learning rate if improvement stops
        'win': 7, # number of words in the context window
        'bs': 9, # number of backprop through time steps
        'nhidden': 100, # number of hidden units
        'seed': 345,
        'emb_dimension': 100, # dimension of word embedding
        'nepochs': 50}

    train_x, train_y, token2idx, idx2token = preprocess_dataset()

    vocsize = len(token2idx)
    nclasses = 50
    nsentences = len(train_x)

    ### instanciate the model
    np.random.seed(s['seed'])
    random.seed(s['seed'])
    rnn = ElmanRNN(nh = s['nhidden'],
                nc = nclasses,
                ne = vocsize,
                de = s['emb_dimension'],
                cs = s['win'] )

    s['clr'] = s['lr']
    for e in xrange(s['nepochs']):
        # shuffle
        shuffle([train_x, train_y], s['seed'])
        s['ce'] = e
        tic = time.time()
        for i in xrange(nsentences):
            cwords = contextwin(train_x[i], s['win'])
            words = map(lambda x: np.asarray(x).astype('int32'), minibatch(cwords, s['bs']))
            labels = train_y[i]
            for word_batch, label_last_word in zip(words, labels):
                rnn.train(word_batch, label_last_word, s['clr'])
                rnn.normalize()
            if s['verbose']:
                print '[learning] epoch %i >> %2.2f%%'%(e,(i+1)*100./nsentences),'completed in %.2f (sec) <<\r'%(time.time()-tic),
                sys.stdout.flush()

    return rnn
