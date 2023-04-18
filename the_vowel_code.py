def encode(st):
    st = st.replace('a', '1')
    st = st.replace('e', '2')
    st = st.replace('i', '3')
    st = st.replace('o', '4')
    st = st.replace('u', '5')
    return st
def decode(st):
    st = st.replace('1', 'a')
    st = st.replace('2', 'e')
    st = st.replace('3', 'i')
    st = st.replace('4', 'o')
    st = st.replace('5', 'u')
