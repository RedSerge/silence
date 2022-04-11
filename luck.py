("""
Down below, words disappear before they are written. Silence under a still pool, no signs of drowning men nor their resistance.
Up above, Aesopian language ain’t appreciated by modern Gagarin followers, either.
In that case, what can a {} developer say nowadays? A little, I guess. Yet, some hex calculations can still bring necessary relief to his anxious mind. Something simple, an exercise, like 
""".format([chr(int(i*0x50)) for i in [1.025, 1.4625] + [1.4375] * 2 + [1.3125, 1.2125, 1.375]]) * 0).join([hex(-reduce(lambda a, b: int(b, 0x10) - int(a, 0x10), i))[0x2:].zfill(0x2) + ("\x2f" if n in (0x5,) else '') for n, i in enumerate(zip(["\x46" * 2] * 0xF, re.findall("..", "\x46\x46\x41\x38\x34\x37\x30\x30\x32\x38\x46\x46"+"\x30"*0x6+"\x46\x46\x37\x43\x32\x39"+"\x30"*0x6)))]).upper() + (""", you know?
Keep exercising, one step per day. Good luck.""" * 0)
