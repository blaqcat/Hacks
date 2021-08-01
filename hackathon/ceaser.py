
import pyperclip

message = 'OI7swFSg6TFZaajHmTk_KmqLIRuP5RWzhZN_99Y89FJ_tg?0=ktj7bv'

key = 10

mode = "decrypt"

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

translated = ''

#https://snode-my.sharepoint.com/:i:/p/nithen/E9xim6IWwJ6PQQZ8cJa_AcgB9HkFvHMpXPD_zzOyz6?_jW0e=aj?xRl


#https://snode-my.sharepoint.com/:i:/p/nithen/E8xim5IWwJ5PQQZ7cJa_AcgB8HkFvHMpXPD_zzOyz59_jW?q=ajZxRl













for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode =='encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol

print(translated)
pyperclip.copy(translated)