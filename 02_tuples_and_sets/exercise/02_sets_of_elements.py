# Option 1
n_length, m_length = map(int, input().split())

n = {input() for _ in range(n_length)}
m = {input() for _ in range(m_length)}

print(*(n.intersection(m)), sep='\n')

# Option 2
# n_length, m_length = map(int, input().split())
# print(*({input() for _ in range(n_length)}.intersection({input() for _ in range(m_length)})), sep='\n')
