import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import leastsq
import numpy, scipy.optimize

# import pylab as plt

def time_samples (seconds = 1e5):
    sample_time = 3e-3
    samples_second = 1/sample_time 
    n = int(samples_second*seconds)
    n_1000 = int(samples_second*1000)
    
    t =np.arange(n)*sample_time
    return t,n_1000

def simulate_noise(t,T=86):
    kappa = 2.7e-6 
    noise_power = 4.4e-25 #brownian motion
    amplitude_noise = np.sqrt(2*noise_power*T/kappa)
    print('noise amplitude = ',amplitude_noise,' [rad]')
    
    # noise distribution - normal
    noise = np.random.uniform(-amplitude_noise, amplitude_noise, t.shape[0])    
    normal([loc, scale, t.shape[0]])
    return noise

def simulate_signal(t,T=86,A=1E-5):
        
    omega = 2*np.pi/T
    y = A* np.cos(omega*t)    
    noise = simulate_noise(t,T)   
    y_noise = y+noise
    
    return y_noise,y





def fit_sin(tt, data):
    '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
    tt = numpy.array(tt)
    yynoise = numpy.array(data)
    ff = numpy.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
    Fyy = abs(numpy.fft.fft(yynoise))
    guess_freq = abs(ff[numpy.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
    guess_amp = numpy.std(yynoise) * 2.**0.5
    guess_offset = numpy.mean(yynoise)
    guess = numpy.array([guess_amp, 2.*numpy.pi*guess_freq, 0., guess_offset])

    def sinfunc(t, A, w, p, c):  return A * numpy.sin(w*t + p) + c
    popt, pcov = scipy.optimize.curve_fit(sinfunc, tt, yynoise, p0=guess)
    A, w, p, c = popt
    f = w/(2.*numpy.pi)
    fitfunc = lambda t: A * numpy.sin(w*t + p) + c
    return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": numpy.max(pcov), "rawres": (guess,popt,pcov)}

def estimate_data(n,t,y,y_noise,integeation_num=0):
    n1 = n*(integeation_num)
    n2 = n*(integeation_num+1)
    
    res = fit_sin(t[n1:n2], y_noise[n1:n2])

    
    print( "Amplitude=%(amp)s, period.=%(period)s, phase=%(phase)s, offset=%(offset)s" % res )
    plt.plot(t[n1:n2], y_noise[n1:n2], "ok", label="y with noise")
    plt.plot(t[n1:n2], y[n1:n2], "-k", label="y", linewidth=2)
    plt.plot(t[n1:n2], res["fitfunc"](t[n1:n2]), "r-", label="y fit curve", linewidth=2)
    plt.legend(loc="best")
    plt.show()

t,n_1000= time_samples (seconds = 1e5)
undamped_noise,undamped = simulate_signal(t,T=86,A=1E-5)
damped_noise,damped = simulate_signal(t,T=40,A=5e-8)
damped_noise1,damped1  = simulate_signal(t,T=20,A=1e-10)

num=3
# estimate_data(n_1000,t,undamped,undamped_noise,num)
# estimate_data(n_1000,t,damped,damped_noise,num)
estimate_data(n_1000,t,damped1,damped_noise1,num)


















