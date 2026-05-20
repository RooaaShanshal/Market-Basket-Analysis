import pandas as pd
from itertools import combinations
from collections import defaultdict

shoptransactions = [
    ["a", "b", "c", "d"],
    ["b", "c", "e", "f"],
    ["a", "d", "e", "f"],
    ["a", "e", "f"],
    ["b", "d", "f"],
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


def apriori(transactions, min_support = 0.3):
    single_items = defaultdict(int)
    for t in transactions:
        for item in t:
            single_items[item] += 1

        num_transactions = len(transactions)

        # 1-itemsets
        L1 = set()
        support_data = {}
        for item, count in single_items.items():
            support = count/num_transactions
            if support >= min_support:
                L1.add((item,))
                support_data[(item,)]=support
        all_frequents = list(L1)
        k=2
        Lk = L1

        while Lk:
            candidates = generate_candidates(Lk, k)
            Lk = set()

            for c in candidates:
                support = get_support(c, transactions)
                if support >= min_support:
                    Lk.add(c)
                    support_data[c] = support
            all_frequents.extend(Lk)
            k += 1
    return all_frequents, support_data


frequent_itemsets, support_data = apriori(shoptransactions, min_support=0.3)

print("Frequent Itemsets:")
for itemset in frequent_itemsets:
    print(itemset, support_data[itemset])
