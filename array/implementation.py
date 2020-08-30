
class MyArray(object):

    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data.get(index)

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        deleted_item = self._left_shift_items(index)
        return deleted_item

    def insert(self, index, item):
        self._right_shift_items(index)
        self.data[index] = item
        return self.length

    def _left_shift_items(self, index):
        deleted_item = self.data[index]
        del self.data[index]
        if index < self.length - 1:
            for i in range(index, self.length - 1):
                self.data[i] = self.data[i + 1]
            del self.data[self.length - 1]

        self.length -= 1
        return deleted_item

    def _right_shift_items(self, index):
        for i in range(self.length - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]
        del self.data[index]
        self.length += 1

    def __repr__(self):
        data = [self.data[i] for i in range(self.length)]
        return "{0}, length={1}".format(data, self.length)


arr1 = MyArray()
arr1.push('hi')
arr1.push('!')
arr1.push('you')
arr1.push('are')
arr1.push('nice')

print(arr1)
print(arr1.get(2) == 'you')

arr1.delete(4)
print(arr1)

# arr1.pop()
# print(arr1)

arr1.insert(2, 'so')
arr1.insert(3, 'awesome')
print(arr1)
