try:
    uchr = unichr
except NameError:
    uchr = chr

message_list = [ u'Circle is 360\u00B0',
               u'Hyv\u00E4\u00E4 \u00FC\u00F6t\u00E4',
               u'\u0989\u09C4 \u09F0 \u09FA \u099F \u09EB \u09EA \u09B9' ]

message1 = message_list[0]
message2 = message_list[1]
message3 = message_list[2]

messages = ', '.join(message_list)

sect = uchr(167)
auml = uchr(228)
ouml = uchr(246)
uuml = uchr(252)
yuml = uchr(255)
