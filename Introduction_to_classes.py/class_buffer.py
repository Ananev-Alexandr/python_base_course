class Buffer:
    def __init__(self):
        self.buf = []
    def add(self, *list_new_num): 
            for num in list_new_num:
                if len(self.buf) <= 4:
                    self.buf.append(num)
                    if len(self.buf) == 5:
                        print(sum(self.buf[:5]))
                        del self.buf[:5]
                else:
                    print(sum(self.buf[:5]))
                    del self.buf[:5]
                    self.buf.append(num)        
    def get_current_part(self):
        return self.buf
