1. Найти имя активити раздела настроек разработчика.

В командной строке в момент, когда открыты настройки разработчика:
adb shell dumpsys activity | findstr mResumedActivity
В результате выводит:
mResumedActivity: ActivityRecord{875ac62 u0 com.android.settings/.SubSettings t9204}
Из чего делаем вывод, что активити называется "SubSettings"

2. Для Dingtone 6.1.0 найти:
a) package name

Способ 1: с включенным приложением написать команду в консоль: adb shell dumpsys activity | findstr mResumedActivity. Первая часть до слеша в фигурных скобках – название идентификатора приложения.

Способ 2: с помощью приложения на android «App inspector» или любого аналогичного.

Способ 3: с помощью команды «adb shell pm list packages» в консоли. В таком случае она выводит идентификаторы всех приложений, и найти Dingtone можно либо введя в поиске (Ctrl + F) слово "dingtone", либо добавив в изначальную команду « | findstr dingtone».

Итог всех трёх способов: me.dingtone.app.im

b) стартовое активити приложения

При запуске приложения вовремя отправить команду в cmd:
adb shell dumpsys activity | findstr mResumedActivity
При запуске это будет:    
mResumedActivity: ActivityRecord{24fb19c u0 me.dingtone.app.im/.activity.SplashActivity t9189}
При главном экране приложения:   
mResumedActivity: ActivityRecord{85da2d4 u0 me.dingtone.app.im/.activity.MainDingtone t9189}
Что доказывает, что активити главного экрана и активити, которое открывается при запуске – разные, и название последнего – "activity.SplashActivity"

c) перечень разрешений, запрашиваемых приложением

Способ 1: выгрузить apk-файл приложения, для этого:
•	"adb shell pm path me.dingtone.app.im" – узнает путь до apk
•	"adb pull <путь, который узнали в предыдущей команде>" - копирует apk на ПК
Затем - "aapt dump permissions <путь до apk на компьютере>"
Способ 2: 
adb shell dumpsys package me.dingtone.app.im
Выводит всю информацию по приложению. В поиске (Ctrl + F) находим "requested permissions"

В итоге получаем:
uses-permission: name='android.permission.SYSTEM_ALERT_WINDOW'
uses-permission: name='android.permission.CALL_PHONE'
uses-permission: name='android.permission.READ_PHONE_STATE'
uses-permission: name='android.permission.READ_PHONE_NUMBERS'
uses-permission: name='android.permission.WRITE_EXTERNAL_STORAGE'
uses-permission: name='android.permission.READ_EXTERNAL_STORAGE'
uses-permission: name='android.permission.VIBRATE'
uses-permission: name='android.permission.INTERNET'
uses-permission: name='android.permission.WAKE_LOCK'
uses-permission: name='android.permission.ACCESS_WIFI_STATE'
uses-permission: name='android.permission.ACCESS_NETWORK_STATE'
uses-permission: name='android.permission.CAMERA'
uses-permission: name='android.permission.RECORD_AUDIO'
uses-permission: name='android.permission.READ_CONTACTS'
uses-permission: name='android.permission.WRITE_CONTACTS'
uses-permission: name='android.permission.MODIFY_AUDIO_SETTINGS'
uses-permission: name='android.permission.BLUETOOTH'
uses-permission: name='android.permission.FOREGROUND_SERVICE'
uses-permission: name='android.permission.RECEIVE_BOOT_COMPLETED'
uses-permission: name='android.permission.ACCESS_FINE_LOCATION'
uses-permission: name='android.permission.ACCESS_COARSE_LOCATION'
uses-permission: name='android.permission.SCHEDULE_EXACT_ALARM'
uses-permission: name='com.google.android.gms.permission.AD_ID'
uses-permission: name='com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE'
uses-permission: name='com.google.android.c2dm.permission.RECEIVE'
uses-permission: name='com.android.vending.BILLING'







