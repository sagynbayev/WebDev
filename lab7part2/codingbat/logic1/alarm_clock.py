def alarm_clock(day, vacation):
    pronto = "7:00" if not vacation else "10:00"
    tarde = "10:00" if not vacation else "off"
    return pronto if day not in [6,0] else tarde
