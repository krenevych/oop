# Warning: to use this program install module keyboard.
# You can install the module keyboard from command line
# >> pip3 install keyboard
# or use pycharm buildin installer.
import keyboard


class KeyboardSpy:

    def __init__(self):
        pass

    def main(self):
        while True:
            try:
                key = keyboard.read_key()
                if keyboard.is_pressed("ctrl") and key == "q":  # To finish use "ctrl+q".
                    print('Finished!')
                    break
                # TODO: notify you listeners here.
            except:
                break


if __name__ == "__main__":
    keyboardSpy = KeyboardSpy()

    # TODO: Register you listeners here

    keyboardSpy.main()
