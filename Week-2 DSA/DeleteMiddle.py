st = []
st.append('1')
st.append('2')
st.append('3')
st.append('4')
st.append('5')
st.append('6')
st.append('7')
 
v = []
 
while(len(st) > 0):
    v.append(st[0])
    del st[0]
     
n = len(v)
 

target = n//2
for i in range(0, n):
    if i==target:
        continue
st.append(v[i])