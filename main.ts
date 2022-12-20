input.onButtonPressed(Button.A, function () {
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
    pins.servoSetPulse(AnalogPin.P1, 0)
    pins.servoSetPulse(AnalogPin.P2, 0)
})
function test (testolcd: string, n: number, pin: number, potenza: number) {
    makerbit.showStringOnLcd1602(testolcd, makerbit.position1602(LcdPosition1602.Pos1), 16)
    basic.showNumber(n)
    if (pin == 1) {
        pins.servoWritePin(AnalogPin.P1, potenza)
    } else {
        pins.servoWritePin(AnalogPin.P2, potenza)
    }
}
input.onButtonPressed(Button.B, function () {
    makerbit.showStringOnLcd1602("reimposto", makerbit.position1602(LcdPosition1602.Pos1), 16)
    pins.servoSetPulse(AnalogPin.P1, 0)
    pins.servoSetPulse(AnalogPin.P2, 0)
})
makerbit.connectLcd(39)
makerbit.showStringOnLcd1602("ok pronto", makerbit.position1602(LcdPosition1602.Pos1), 16)
