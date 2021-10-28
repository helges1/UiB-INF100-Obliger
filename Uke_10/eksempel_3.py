# IO-part (placing the data into a data structure)
# =====================================================

with open("alice.txt", encoding="utf8") as f:
    text = f.read()

# =====================================================


### resten er lik programmet fra før
# data processing/analysis
# =====================================================

letter_count = {}

for l in "abcdefghijklmnopqrstuvwxyz":
    letter_count[l] = 0

for let in text:
    let = let.lower()
    if let in letter_count:
        letter_count[let] += 1

# =====================================================

# IO-part (presenting the results)
# =====================================================

for let, count in letter_count.items():
    print(f"{let} is used {count:5d} times")


print("\n\n\n")

# =====================================================

# data processing/analysis
# =====================================================

word_count = {}

for word in text.split():
    word = word.lower()
    word_count.setdefault(word, 0)
    word_count[word] += 1


def get_second(tpl):
    return tpl[1]


sorted_result = sorted(word_count.items(), key=get_second, reverse=True)

# =====================================================

# IO-part (presenting the results)
# =====================================================

N = 15
print(f"The {N} most common words")
for w, c in sorted_result[:N]:
    print(f"{w:14} is used {c:5d} times")

# =====================================================
