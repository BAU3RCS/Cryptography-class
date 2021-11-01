#message = '65698332751011215832698367658069'
message='691181011103210510232121111117114321121141051091011153297114101321089711410310132116104101328283653299971103298101329811411110710111032119104101110321091051151169710710111532971141013210997100101'

def getmessage(message):
   q = int(message)
   flag = []
   while q > 0:
      qmod = q % 100
      if qmod < 30:
         flag.insert(0,chr(q % 1000))
         q = q // 1000
      else:
         flag.insert(0,chr(qmod))
         q = q // 100
   print(''.join(flag))
getmessage(message)
