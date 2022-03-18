# textfile creation


txtfile = open("D:\sample\kk.txt","w")
s = ('res \nhma \n')
a = ('kar \nun')
txtfile.writelines((s, a))

txtfile.flush() #to clear the internal buffer