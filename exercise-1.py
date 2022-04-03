duration = int(input('Enter all the time in seconds: '))
if duration < 60:
    seconds = duration % 60
    print('seconds: ', seconds, sep='')
elif 3600 > duration > 60:
    minutes = duration // 60 % 60
    seconds = duration % 60
    print('minutes: ', minutes, ', ', 'seconds: ', seconds, sep='')
elif duration % 60 == 0:
    minutes = duration // 60 % 60
    print('minutes: ', minutes, sep='')
elif 3600 < duration < 3600 * 24:
    hours = duration // 3600
    minutes = duration // 60 % 60
    seconds = duration % 60
    print('hours: ', hours, ', ' 'minutes: ', minutes, ', ', 'seconds: ', seconds, sep='')
elif duration > 3600 * 24:
    days = duration // 3600 // 24
    hours = duration // 3600 - days * 24
    minutes = duration // 60 % 60
    seconds = duration % 60
    print('days: ', days, ', ', 'hours: ', hours, ', ', 'minutes: ', minutes, ', ', 'seconds: ', seconds, sep='')
