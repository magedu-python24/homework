#

[ print("{}*{}={:<2}".format(j,i,i*j),end='\n' if i==j else ' ') for i in range(1,10) for j in range(1,i+1) ]

print()

[ print("{}*{}={:<2}".format(' '*7*(i-1)+str(i) if i==j else i,j,i*j),end='\n' if 9==j else ' ') for i in range(1,10) for j in range(i,10) ]
