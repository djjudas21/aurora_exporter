# Aurora node exporter

Set baud rate
```
stty -F /dev/ttyUSB0 19200
```

```
jonathan@rpi:~/aurora$ ls -la /dev/ttyUSB0 
crw-rw---- 1 root dialout 188, 0 Mar  6 20:31 /dev/ttyUSB0
```

Standard realtime stats:

```
sudo aurora -a 2 -d 0 /dev/ttyUSB0 

Input 1 Voltage             =    202.644669 V
Input 1 Current             =      0.468859 A
Input 1 Power               =     95.011826 W

Input 2 Voltage             =    201.899002 V
Input 2 Current             =      0.446302 A
Input 2 Power               =     90.108009 W

Grid Voltage Reading        =    243.262344 V
Grid Current Reading        =      0.854146 A
Grid Power Reading          =    188.479767 W
Frequency Reading           =     50.050049 Hz.

DC/AC Conversion Efficiency =         101.8 %
Inverter Temperature        =     29.993212 C
Booster Temperature         =     28.770926 C
```

Column output format:

```
sudo aurora -a 2 -d 0 -c /dev/ttyUSB0 
   201.624283       0.445497      89.822975     201.742020       0.425357      85.812340     243.456573       0.803760     178.681992      50.022011     101.734665      29.787601      28.327892    OK`
```


Extended stats:

```
sudo aurora -a 2 -D /dev/ttyUSB0 

Extended DSP Reporting
Vbulk                           =  381.726715 V
Isolation Resistance (Riso)     =   18.190901 Mohm
Power Peak Today                = 2408.548096 W  
Pin 1                           =   93.037354 W
Pin 2                           =   88.419197 W

Vbulk Mid                       =  187.096313 V  
Vbulk (Dc/Dc)                   =  384.865906 V

Ileak (Dc/Dc) Reading           =    0.000000 A
Ileak (Inverter) Reading        =    0.000000 A

Grid Voltage (Dc/Dc)            =  243.965729 V
Grid Voltage Average (VgridAvg) =  243.541489 V  
Grid Voltage neutral            =  301.355255 V  
Grid Frequency (Dc/Dc)          =   50.014004 Hz

Power Peak                      = 3254.749756 W  
Wind Generator Frequency        =    0.000000 Hz 
```

Dir for prom output text files: `/var/lib/prometheus/node-exporter`
