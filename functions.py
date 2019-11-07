from psutil import sensors_battery
from win10toast import ToastNotifier
from time import sleep
from threading import Thread

toaster = ToastNotifier()


def check(plugged, percent):
    if plugged == False:

        if int(percent) <= 15:
            toaster.show_toast("Battery Tracker",
                               '{}%, Not Plugged In. need juice'.format(percent))

        if int(percent) > 90:
            toaster.show_toast("Battery Tracker",
                               '{}%, Not Plugged In. good.'.format(percent))

        if int(percent) > 80:
            toaster.show_toast("Battery Tracker",
                               '{}%, Not Plugged In. still good.'.format(percent))

        if int(percent) < 80 and int(percent) > 50:
            toaster.show_toast("Battery Tracker",
                               '{}%, Not Plugged In. fine.'.format(percent))

    else:
        if int(percent) > 90:
            msg[1] = '{}%, enough.'.format(percent)
            toaster.show_toast("Battery Tracker",
                               '{}%, Plugged In. enough.'.format(percent, msg))

        if int(percent) > 80:
            toaster.show_toast("Battery Tracker",
                               '{}%, Plugged In. almost there.'.format(percent))


def getBattery():
    battery = sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    return [plugged, percent]


def watchLowerHigher():
    while True:
        plugged, percent = getBattery()

        if plugged == False:
            if int(percent) <= 15:
                toaster.show_toast("Battery Tracker",
                                   '{}%, need juice.'.format(percent))
        else:
            if int(percent) > 90:
                toaster.show_toast("Battery Tracker",
                                   '{}%, enough.'.format(percent))


def watchHourly(SECS):
    count = 0

    while True:
        msg = ''
        count = count + 1
        sleep(SECS)
        plugged, percent = getBattery()
        check(msg, plugged, percent)

        print('executed: {}.'.format(count))


def start(SECS):
    t1 = Thread(target=watchHourly, args=[SECS])
    t2 = Thread(target=watchLowerHigher)

    t1.start()
    t2.start()
