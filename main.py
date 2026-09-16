# ============================================================
# 專案名稱：micro:bit 閃紅燈
# 目標板：BBC micro:bit V2
# 週邊：3-Pin 紅色 LED 模組
#
# 接線（請對照模組絲印，不要憑顏色猜）：
#   LED IN  -> micro:bit P1（金色金手指，標示 1）
#   LED VCC -> micro:bit 3V（標示 3V，約 3.3V）
#   LED GND -> micro:bit GND
#
# 功能：以 500ms 高電位、500ms 低電位讓 P1 外接紅燈持續閃爍。
# ============================================================

from microbit import *

# ---------- 可調參數 ----------
# sleep() 的單位是「毫秒」，不是秒。
# 500 + 500 = 1000ms，視覺上約每秒閃一次（1 Hz）。
ON_MS = 500
OFF_MS = 500

# ---------- 腳位宣告（軟體除錯時最先檢查這裡）----------
# MicroPython 要用 pin1 物件，不能寫 pin.P1 或字串 "P1"。
# V2 的 P0 / P1 / P2 都可做數位輸出；本專案固定使用 P1。
LED_PIN = pin1

# 多數 3-Pin LED 模組是「高電平觸發」：IN=1 亮、IN=0 滅。
# 若你的模組說明寫 Low Level Trigger，把下面兩個值對調即可。
LEVEL_ON = 1   # 高電位，約 3.3V
LEVEL_OFF = 0  # 低電位，0V


def led_on():
    """把 P1 拉高，點亮外接 LED；同時點陣顯示愛心方便確認程式有在跑。"""
    LED_PIN.write_digital(LEVEL_ON)
    display.show(Image.HEART)


def led_off():
    """把 P1 拉低，熄滅外接 LED；點陣清空。"""
    LED_PIN.write_digital(LEVEL_OFF)
    display.clear()


# ---------- 開機自我檢查 ----------
# 先顯示「1」，代表這份韌體是「P1 閃燈」版本，用來確認 .hex 真的燒進去。
display.show("1")
sleep(800)
led_off()
sleep(200)

# ---------- 主迴圈 ----------
# 必須是無窮迴圈，閃爍才會一直重複。
# 每次改變電位後一定要 sleep()：
#   1. 沒有延遲時切換太快，肉眼會覺得燈一直亮。
#   2. 忙等會讓 CPU 滿載，USB / REPL 變得不穩。
while True:
    led_on()
    sleep(ON_MS)

    led_off()
    sleep(OFF_MS)
