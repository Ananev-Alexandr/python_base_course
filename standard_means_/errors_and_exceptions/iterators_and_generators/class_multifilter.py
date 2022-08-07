class multifilter:

    def judge_half(pos, neg):
        if (pos >= neg):
            return True

    def judge_any(pos, neg):
        if (pos >= 1):
            return True

    def judge_all(pos, neg):
        if (neg == 0):
            return True

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.judge = judge
        self.funcs = funcs

    def __iter__(self):
        list_ = []
        for elem in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(elem) is True:
                    pos += 1
                else:
                    neg += 1

            if self.judge(pos, neg) is True:
                list_.append(elem)
        return iter(list_)
