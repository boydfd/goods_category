import jieba
import jieba.posseg as pseg

seg_list = jieba.cut("CONSOL")
res = "潮流男包"


def get_noun(words):
    return [word for word, flag in words if flag in ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns",
                                                     "nsf", "nt", "nz", "nl", "ng"]]


noun = get_noun(pseg.cut(res))
print(list(noun))
# print(sum(1 for _ in seg_list))
print(list(seg_list))
print("Full Mode: " + "/ ".join(seg_list))  # 全模式
