from re import *
tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
words=tweets.split()
rule="[@][a-zA-z0-9]+"
# for w in words:
#     matcher=fullmatch(rule,w)
#     if matcher!=None:
#         print(w)



matcher=finditer(rule,tweets)
for m in matcher:
    print(m.group())

