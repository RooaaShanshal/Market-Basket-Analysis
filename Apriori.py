import pandas as pd
from itertools import combinations
from collections import defaultdict

shoptransactions = [
    ["milk", "bread", "eggs"],
    ["milk", "bread"],
    ["milk", "diapers", "beer", "eggs"],
    ["bread", "butter"],
    ["milk", "bread", "butter"],
    ["diapers", "beer"],
    ["milk", "bread", "butter", "eggs"],
]


def get_support(itemset, transactions):
    count = 0
    for t in transactions:
        if set(itemset).issubset(set(t)):
            count += 1
    return count / len(transactions)


def generate_candidates(prev_frequent_itemsets, k):
    candidates = set()
    prev_list = list(prev_frequent_itemsets)

    for i in range(len(prev_list)):
        for j in range(i + 1, len(prev_list)):
            union_set = tuple(sorted(set(prev_list[i]) | set(prev_list[j])))
            if len(union_set) == k:
                candidates.add(union_set)
    return candidates
