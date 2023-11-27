import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.gridspec as gridspec

fig = plt.figure()
gs = gridspec.GridSpec(2, 2, height_ratios=[2, 1])

# Интерактивное окно для первой волны
ax_wave1 = plt.subplot(gs[0, 0])
ax_wave1.set_title('Wave 1')
ax_wave1.set_xlim(0, 2 * np.pi)
ax_wave1.set_ylim(-1, 1)
line_wave1, = ax_wave1.plot([], [], lw=2)

# Интерактивное окно для второй волны
ax_wave2 = plt.subplot(gs[0, 1])
ax_wave2.set_title('Wave 2')
ax_wave2.set_xlim(0, 2 * np.pi)
ax_wave2.set_ylim(-1, 1)
line_wave2, = ax_wave2.plot([], [], lw=2)

# Окно для отображения результата сложения волн
ax_result = plt.subplot(gs[1, :])
ax_result.set_title('Sum')
ax_result.set_xlim(0, 2 * np.pi)
ax_result.set_ylim(-2, 2)
line_result, = ax_result.plot([], [], lw=2)

# Функция для обновления графиков
def update_wave1(freq1, amp1):
    t = np.linspace(0, 2 * np.pi, 1000)
    wave1 = amp1 * np.sin(freq1 * t)
    line_wave1.set_data(t, wave1)

def update_wave2(freq2, amp2):
    t = np.linspace(0, 2 * np.pi, 1000)
    wave2 = amp2 * np.sin(freq2 * t)
    line_wave2.set_data(t, wave2)

def update_result(freq1, amp1, freq2, amp2):
    t = np.linspace(0, 2 * np.pi, 1000)
    wave1 = amp1 * np.sin(freq1 * t)
    wave2 = amp2 * np.sin(freq2 * t)
    result = wave1 + wave2
    line_result.set_data(t, result)

    fig.canvas.draw_idle()

# Создание слайдеров для настройки параметров волн
slider_ax_freq1 = plt.axes([0.15, 0.15, 0.7, 0.03])
slider_ax_amp1 = plt.axes([0.15, 0.1, 0.7, 0.03])
slider_ax_freq2 = plt.axes([0.15, 0.05, 0.7, 0.03])
slider_ax_amp2 = plt.axes([0.15, 0.0, 0.7, 0.03])

slider_freq1 = Slider(slider_ax_freq1, 'Frequency 1', 0.1, 10.0, valinit=1.0)
slider_amp1 = Slider(slider_ax_amp1, 'Amplitude 1', 0.1, 1.0, valinit=0.5)
slider_freq2 = Slider(slider_ax_freq2, 'Frequency 2', 0.1, 10.0, valinit=2.0)
slider_amp2 = Slider(slider_ax_amp2, 'Amplitude 2', 0.1, 1.0, valinit=0.5)

# Функции обновления при изменении слайдеров
def update_wave1_slider(val):
    update_wave1(slider_freq1.val, slider_amp1.val)
    update_result(slider_freq1.val, slider_amp1.val,
                  slider_freq2.val, slider_amp2.val)

def update_wave2_slider(val):
    update_wave2(slider_freq2.val, slider_amp2.val)
    update_result(slider_freq1.val, slider_amp1.val,
                  slider_freq2.val, slider_amp2.val)

def update_result_sliders(val):
    update_result(slider_freq1.val, slider_amp1.val,
                  slider_freq2.val, slider_amp2.val)

slider_freq1.on_changed(update_wave1_slider)
slider_amp1.on_changed(update_wave1_slider)
slider_freq2.on_changed(update_wave2_slider)
slider_amp2.on_changed(update_wave2_slider)
slider_freq1.on_changed(update_result_sliders)
slider_amp1.on_changed(update_result_sliders)
slider_freq2.on_changed(update_result_sliders)
slider_amp2.on_changed(update_result_sliders)

# Инициализация графиков
update_wave1(slider_freq1.val, slider_amp1.val)
update_wave2(slider_freq2.val, slider_amp2.val)
update_result(slider_freq1.val, slider_amp1.val, slider_freq2.val, slider_amp2.val)

plt.subplots_adjust(hspace=0.5, bottom=0.3)
plt.show()
