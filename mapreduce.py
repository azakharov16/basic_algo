def iter_group(queue):
    buf = []
    prev_key = None

    for val in queue:
        cur_key, cur_val = val
        #print cur_key, cur_val
        if cur_key == prev_key or prev_key is None:
            buf.append(cur_val)
        else:
            yield prev_key, buf
            buf = []
            buf.append(cur_val)
        prev_key = cur_key

    if buf:
        yield cur_key, buf

class MapReduce:
    def __init__(self):
        self.queue = []

    def send(self, a,b):
        self.queue.append((a,b))

    def count(self):
        return len(self.queue)    

    def __iter__(self):
        return iter_group(sorted(self.queue))

x = MapReduce()
for word in "foo bar bar".split():
    x.send(word, 1)

for word, ones in x:
    print word, sum(ones)