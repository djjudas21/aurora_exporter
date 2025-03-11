# Aurora node exporter

This is a small script which takes output from the [`aurora`](http://www.curtronics.com/Solar/AuroraData.html) program and reformats
it as Prometheus metrics which can be collected via the textfile collector on a
[Prometheus node exporter](https://github.com/prometheus/node_exporter).

You will need :
- a USB to RS-485 interface [connected up to your Power One Aurora inverter](http://francescopaganelli.blogspot.com/2013/01/how-connect-raspberry-pi-to-aurora-uno.html)
- the `aurora` binary, built from source or installed from [package on Ubuntu](https://launchpad.net/aurora)
- a system which is running the Prometheus node exporter

Before we start, explicitly set baud rate:
```console
stty -F /dev/ttyUSB0 19200
```

Experiment with the `aurora` program directly to verify it is working. Make sure
you are talking to the right serial device `/dev/ttyUSB0` and the right inverter
address `-a 2`. Once you get output like this, you can proceed.

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

Add the following line to `/etc/crontab`, making sure to update the path to
this script. This runs `aurora` every minute, reformats as Prometheus metrics,
and writes it atomically with `sponge` to
`/var/lib/prometheus/node-exporter/aurora.prom` where it will be picked up by
the node exporter.

```
* * * * *	root	aurora -a 2 -d 0 -Y 3 /dev/ttyUSB0 | /home/jonathan/aurora_exporter/aurora.py | sponge /var/lib/prometheus/node-exporter/aurora.prom
```
