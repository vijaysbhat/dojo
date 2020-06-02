'''
Count the number of score combinations in an American football game 
that add up to the final score s given possible plays with scores
W e.g. W = [2,3,7]

Notes:
* for distinct play sequences, eliminate one play score at a time in the recursion forumula
* for combinations of scores, find a way to dedupe play sequences with the same plays (but different order).
* what went right
    * remembered to copy list retrieved from DP memo instead of using the original object since it could have unpredictable results
      if they get reused across recursive calls.
* what went wrong
    * in Python list append doesn't return the value of the augmented list
    * constructing a dict of dicts is tricky since we need a way to hash each individual dictionary
        * one way is to sort the dict and convert to string 
'''
from copy import copy
import json

def play_sequences(s, W, memo):
    plays = []
    for w in W:
        if s == w:
            plays.append([w])
        if s - w > 0:
            if s - w in memo:
                sub_plays = memo[s-w]
            else:
                sub_plays = play_sequences(s - w, W, memo)
                memo[s-w] = sub_plays

            for p in sub_plays:
                p = copy(p)
                p.append(w)
                plays.append(p)
    return plays

def score_combination_key(sc):
    sorted_sc = {k : sc[k] for k in sorted(sc.keys())}
    return json.dumps(sorted_sc)

def score_combinations(s, W, memo):
    scores_dict = {}
    for w in W:
        if s == w:
            sc = {w: 1}
            scores_dict[score_combination_key(sc)] = sc
        if s - w > 0:
            if s - w in memo:
                sub_scores = memo[s-w]
            else:
                sub_scores = score_combinations(s - w, W, memo)
                memo[s-w] = sub_scores

            for sc in sub_scores.values():
                sc = copy(sc)
                if w in sc.keys():
                    sc[w] += 1
                else:
                    sc[w] = 1
                scores_dict[score_combination_key(sc)] = sc
    return scores_dict

if __name__ == '__main__':
    W = [2,3,7]
    test_cases = [12, 13, 30]
    for t in test_cases:
        plays = play_sequences(t, W, {})
        scores = score_combinations(t, W, {})
        print('Score', t, 'Number of play sequences:', len(plays), 'Number of score combinations:', len(scores))

