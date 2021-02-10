#!/bin/env python

import markovify


def make_chain(input_file):
  with open(input_file) as f:
    text = f.read()
  
  text_model = markovify.NewlineText(text)

  return text_model


def generate(file_name):
  model = make_chain(file_name)
  return model.make_sentence()


if __name__ == '__main__':
  for i in range(5):
    sentence = generate('data/data.csv')
    print(sentence)

