class Language:
    """Define how to say things in a language"""

    def __init__(self, Name: str, Greeting: str, Thanks: str):
        """__init__"""
        self._name = Name
        self._greeting = Greeting
        self._thanks = Thanks

    def get_name(self):
        """Name Getter"""
        return self._name

    name = property(get_name)

    def __eq__(self, other):
        """__eq__"""
        return self.name == other.name

    def get_greeting(self):
        """Greeting Getter"""
        return self._greeting

    greeting = property(get_greeting)

    def get_thanks(self):
        """Thanks Getter"""
        return self._thanks

    thanks = property(get_thanks)

def main():
    German = Language("German", "Hallo", "Danke")
    print(German.thanks)

    Chinese = Language("中文", "你好", "谢谢")
    print(Chinese.name)
    print(Chinese.greeting)
    print(Chinese.thanks)

if __name__ == "__main__":
    main()