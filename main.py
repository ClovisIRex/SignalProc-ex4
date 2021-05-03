import numpy as np
import matplotlib.pyplot as plt
from os.path import dirname, join as pjoin
import sounddevice as sd
from scipy.io import loadmat


# 2

def cross_correlation(first, second):
    # zero padding, so both will be the same size
    if len(first) > len(second):
        while len(first) > len(second):
            second.append(0)
    elif len(first) < len(second):
        while len(first) < len(second):
            first.append(0)
    num_of_vals = 2 * len(second) - 1
    corr = [0] * num_of_vals
    index = 0
    for x in range(num_of_vals):
        val = x - len(second) + 1
        for i in range(len(first)):
            if len(second) > (i + val) >= 0:
                p = first[i] * second[i + val]
                corr[index] += p
        index += 1
    return corr

vectora = np.array([3, 2, 1])
vectorb = np.array([6, 5, 4])

# testing that np.correlate and our code produces same result
our_xcorr_arr = np.array(cross_correlation(vectora, vectorb))
builtin_xcorr_arr = np.correlate([6,5,4], [3,2,1], 'full')

np.testing.assert_equal(our_xcorr_arr, builtin_xcorr_arr)



#3

# plotting w/noise
t = np.arange(0, 2, 0.01)
x = np.sin(t*(20 * np.pi)) + np.random.rand(len(t))

fig = plt.figure()
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.title('sin(20pi*t + rand(1, length(t))')
plt.plot(x[:len(t)])
plt.show()

# plotting with smoothing using rec. window
q = 0.2 * np.ones(5)
z = cross_correlation(x.tolist(), q.tolist())
# print (len(z))
# z = np.correlate(x, q)
fig = plt.figure()
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.title('sin(20pi*t + rand(1, length(t)) smoothed by rectangular window (N=5)')
plt.plot(z[:len(t)])
plt.show()



# 6


music = loadmat("ccMusic.mat")
fs = 44100
hurt = music.get('yHurt').T
silence = music.get('ySilence').T
heathens = music.get('yHeathens').T
snip = music.get('ySnip').T


# cc_hurt_snip = cross_correlation(hurt.tolist(), snip.tolist())
sd.play(music.get('yHurt').T, fs)
sd.wait()



