# - get(key: int) -> int:
# - delete(key: int) -> None:
# - put(key: int, value: int) -> None:
#

class Cache:
    def __init__(self):
        self.my_dict = {}

    def pri(self):
        print(self.my_dict)

    def put(self, key, value):
        self.my_dict[key] = value

    def get(self, key):
        return self.my_dict.get(key, None)

    def delete(self, key):
        if key in self.my_dict:
            del self.my_dict[key]


cache = Cache()
cache.put("4", "fdf")
print(cache.get("9"))
cache.delete("9")
cache.put("66", "hello")
cache.pri()
