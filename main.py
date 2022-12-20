def on_button_pressed_a():
    test("P1 step 1", 1, 1, 0)
    basic.pause(3000)
    test("P1 step 2", 2, 1, 180)
    basic.pause(3000)
    test("P3 step 3", 3, 1, 91)
    basic.pause(3000)
    test("P2 step 1", 4, 2, 0)
    basic.pause(3000)
    test("P2 step 2", 5, 2, 180)
    basic.pause(3000)
    test("P2 step 3", 6, 2, 91)
    pins.servo_set_pulse(AnalogPin.P1, 0)
    pins.servo_set_pulse(AnalogPin.P2, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def test(testolcd: str, n: number, pin: number, potenza: number):
    makerbit.show_string_on_lcd1602(testolcd, makerbit.position1602(LcdPosition1602.POS1), 16)
    basic.show_number(n)
    if pin == 1:
        pins.servo_write_pin(AnalogPin.P1, potenza)
    else:
        pins.servo_write_pin(AnalogPin.P2, potenza)

def on_button_pressed_b():
    makerbit.show_string_on_lcd1602("reimposto", makerbit.position1602(LcdPosition1602.POS1), 16)
    pins.servo_set_pulse(AnalogPin.P1, 0)
    pins.servo_set_pulse(AnalogPin.P2, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

makerbit.connect_lcd(39)
makerbit.show_string_on_lcd1602("ok pronto", makerbit.position1602(LcdPosition1602.POS1), 16)