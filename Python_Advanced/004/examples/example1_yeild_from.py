def concat_sequence_v1(s1, s2):
    """
    Склеювання двох послідовностей.
    """
    for elem in s1:
        yield elem
    for elem in s2:
        yield elem


def concat_sequence_v2(s1, s2):
    """
    Аналогічно прикладу concat_sequence_v1 - склеюємо дві послідовності,
    але вже з використанням yield from, що дозволить нам не запускати цикл.
    """
    yield from s1
    yield from s2


seq1 = range(10)
seq2 = range(10, 20)
result = concat_sequence_v1(seq1, seq2)

print('Seq 1')
for i in result:
    print(i)

seq1 = range(10)
seq2 = range(10, 20)
result = concat_sequence_v2(seq1, seq2)

print('Seq 2')
for i in result:
    print(i)
