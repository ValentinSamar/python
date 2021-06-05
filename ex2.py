sec_vsego=int(input("Введите количество секунд"))
hh= sec_vsego // 3600
mm= (sec_vsego-hh*3600)//60
ss= sec_vsego % 60
print("%02d:%02d:%02d" % (hh, mm, ss))

