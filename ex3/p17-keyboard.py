import os
import keyboard

class Keyboard:
    num: list[int] = []

    def press(self, key: str):
        try:
            if len(self.num) >= 9:
                return
            n = int(key)
            self.num.append(n)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{''.join([str(n) for n in self.num])}')
        except ValueError:
            pass

    def backspace(self):
        if len(self.num) > 0:
            self.num.pop()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{''.join([str(n) for n in self.num])}')

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.num = []

kb = Keyboard()

def on_key_release(event):

    if event.name == 'backspace':
        kb.backspace()
    elif event.name == 'enter':
        kb.clear()
    else:
        kb.press(event.name)

if __name__ == '__main__':
    keyboard.on_release(on_key_release)
    keyboard.wait()



