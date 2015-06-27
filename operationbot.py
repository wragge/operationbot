# -*- coding: utf-8 -*-
import random
import inflect
import pickle
import os
import twitter
import credentials

current_dir = os.path.dirname(os.path.realpath(__file__))
p = inflect.engine()

with open(os.path.join(current_dir, 'nouns.pck'), 'rb') as noun_file:
    nouns = pickle.load(noun_file)

with open(os.path.join(current_dir, 'adjs.pck'), 'rb') as adj_file:
    adjs = pickle.load(adj_file)

with open(os.path.join(current_dir, 'verbs.pck'), 'rb') as verb_file:
    verbs = pickle.load(verb_file)

phrases = [
    u'protecting Australia from',
    u'defending Australia’s',
    u'returning Australia’s',
    u'{} illegal'.format(p.present_participle(random.choice(verbs)))
    ]


def create_message():
    return u'Operation {} {} – {} {}'.format(
        random.choice(adjs).title(),
        random.choice(nouns).title(),
        random.choice(phrases),
        p.plural(random.choice(nouns)))


def tweet_operation(api):
    message = create_message()
    while len(message) > 140:
        message = create_message()
    # print message
    api.PostUpdate(message)


if __name__ == '__main__':
    api = twitter.Api(
        consumer_key=credentials.consumer_key,
        consumer_secret=credentials.consumer_secret,
        access_token_key=credentials.access_token_key,
        access_token_secret=credentials.access_token_secret
    )
    tweet_operation(api)
