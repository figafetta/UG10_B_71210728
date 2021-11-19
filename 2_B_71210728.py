RSI = int(input("Masukan besar RSI: "))
MACD = str(input("Masukan kondisi MCD: "))

if RSI >= 70 and MACD == ("death-cross"):
    print("RSI lebih dari sama dengan 70 dan MACD Death-cross, saatnya jual")

elif RSI <= 30 and MACD == ("golden-cross"):
    print("RSI kurang dari sama dengan 30 dan MACD Golden-cross, saatnya beli")

elif RSI >= 70 and MACD == ("golden-cross"):
    print("RSI lebih dari sama dengan 70 dan MACD Golden-cross, Tunggu MACD sampai death-cross")

elif RSI <= 30 and MACD == ("death-cross"):
    print("RSI kurang dari sama dengan 30 dan MACD Death-cross, Tunggu MACD sampai Golden-cross")

elif RSI > 30 < 70 and MACD == ("golden-cross" or "death-cross"):
    print("RSI berada diarea 30 - 70, Bukan saatnya membeli maupun menjual")
    
else:
    print ("error")
    