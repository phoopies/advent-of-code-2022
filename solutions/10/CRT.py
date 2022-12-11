from CPU import CPU


class CRT:
    def __init__(self, sprite_width=3) -> None:
        self.cpu = CPU()
        self.current_sprite_pos = 0
        self.sprite_width = sprite_width

    def draw(self, instructions, width=40, height=6):
        screen = ''
        all_states = []
        for instruction in instructions:
            states = self.cpu.perform(instruction)
            all_states += states
        max_pixels = width * height
        for (register, cycle) in all_states[:max_pixels]:
            print(self.current_sprite_pos, register)
            if register in range(self.current_sprite_pos-1, self.current_sprite_pos + self.sprite_width-1):
                screen += '#'
            else:
                screen += '.'
            self.current_sprite_pos += 1
            if cycle % width == 0:
                screen += '\n'
                self.current_sprite_pos = 0
        print(screen)
