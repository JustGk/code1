sub=int(input("how many subjects are in the list :"))
enter=list(map(int,input("enter the marks :").strip().split()))[:sub]

print(sum(enter))