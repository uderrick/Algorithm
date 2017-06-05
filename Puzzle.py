# -*- coding: utf-8 -*-
import networkx as net
import matplotlib.pyplot as plt
import collections
import Queue

check_lst = Queue.Queue()
G = net.DiGraph()

def show ( arr ):
    print str(arr[0][0])+str(arr[0][1])+str(arr[0][2])
    print str(arr[1][0])+str(arr[1][1])+str(arr[1][2])
    print str(arr[2][0])+str(arr[2][1])+str(arr[2][2])
    
start  = [[1,3,2],
[" ",7,8],
[5,6,4]]
goal = [[1,7,3],
[6,5,2],
[" ",4,8]]

key = 1 # 딕셔너리에서의 키값. 
Dic = {1:start}
#2차원 배열명 : 숫자

def check_find( arr ):#이함수는 bfs 때 goal 배열과의 검사를 위한 함수.
    for i in range(3):
        for j in range(3):
            if arr[i][j] != goal[i][j]:
                return False
    return True
pathh = []
#############################################################
parent = [] # 부모랑 중복되는거 있나 검사하기 위해서!!!
def find( node ):
   
    if node == 1:
        parent.append(Dic[1])
    else:
        d = (G.predecessors( node )).pop(0)
        parent.append(Dic[d])
        find(d)

#####################################################


"""   
# bfs 완벽 이해해야 함.
def bfs(graph, root): 
    
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    puzzle_list = [] #2차원 배열 이름들의 집합.

    while queue: 
        vertex = queue.popleft()
     
        
        puzzle_list = Dic.values()
        for value in puzzle_list:
            if check_find(value) == True:
                print "찾았습니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print value # 그 2차원 배열 보여주기
                return False
                
        ve = int(vertex)
        for neighbour in graph[ve]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour)
                
"""
def bfs(graph, start):
    
    global pathh
 
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        
        # get the first path from the queue
        path = queue.pop(0)
        
        # get the last node from the path
        node = path[-1]
     
        # path found
        if check_find( Dic[node]) == True :
            pathh = path
            return True
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.neighbors(node):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
   
                                    
def child_check( arr ):#이 함수는 자식 노드를 추가해주는 함수.
 
    up_side =[[""for j in range(3)] for i in range(3)]
    up_arr = [[""for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            up_arr[i][j] = arr[i][j]
    
    down_side = [[""for j in range(3)] for i in range(3)]
    down_arr = [[""for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            down_arr[i][j] = arr[i][j]
            
    left_side=[[""for j in range(3)] for i in range(3)]
    left_arr = [[""for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            left_arr[i][j] = arr[i][j]
            
    right_side=[[""for j in range(3)] for i in range(3)]
    right_arr = [[""for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            right_arr[i][j] = arr[i][j]
            
    ##이부분 점검 요망
    i_idx = 0
    j_idx = 0
    
    key_of_parent = 0
    for idx in Dic:
        if Dic[idx] == arr:
            key_of_parent = idx
            
    #부모 노드의 딕셔너리에서의 키값. 이걸 알아야 그래프에 추가할 수 있다.
    for i in range(3):
        for j in range(3):
            if arr[i][j] == " ":
                i_idx = i
                j_idx = j
    
    
    
###############################################################################3    
    if 0<=( i_idx - 1) <=2 and 0<=( j_idx ) <= 2:#공백 블록이 윗칸으로 이동 가능하다는 의미.
        tmp = up_arr[i_idx][j_idx]
   
        up_arr[i_idx][j_idx] = up_arr[i_idx-1][j_idx]
        up_arr[i_idx-1][j_idx] = tmp
     
        for i in range(3):
            for j in range(3):
                up_side[i][j] = up_arr[i][j]
                
        global key
        global parent
        
        upload = False
        find( key )# parent 에다가 조상님들 싹다 넣기.
       
        if up_side not in parent:
            upload = True
                        
        parent = []      
        if( upload == True):
          
            key +=1 #딕셔너리 키값 1증가.
        
            Dic[key] = up_side#딕셔너리에 추가.
        
            G.add_edge(key_of_parent,key)
    
    if 0<=( i_idx ) <=2 and 0<=( j_idx - 1 ) <= 2:#공백 블록이 왼쪽으로 이동 가능하다는 의미.
        ##지금나는 오류 => 위의 if 문을 거치고 나서 arr이 변경되어 버림.
        
        tmp = left_arr[i_idx][j_idx]
       
         # tmp 가 공백이 맞나??? 숫자면 수정해줘야함!!!
        left_arr[i_idx][j_idx] = left_arr[i_idx][j_idx-1]
        left_arr[i_idx][j_idx-1] = tmp
        
        for i in range(3):
            for j in range(3):
                left_side[i][j] = left_arr[i][j]
                
        global key
        global parent
        
        upload = False
        find( key )# parent 에다가 조상님들 싹다 넣기.
        
        if left_side not in parent:
            upload = True
                        
        parent = []      
        if( upload == True):
        
            key +=1 #딕셔너리 키값 1증가.
        
            Dic[key] = left_side#딕셔너리에 추가.
        
            G.add_edge(key_of_parent,key)
        
    if 0<=( i_idx ) <=2 and 0<=( j_idx+1 ) <= 2:#공백 블록이 오른쪽으로 이동 가능하다는 의미.
        tmp = right_arr[i_idx][j_idx]
        
        right_arr[i_idx][j_idx] = right_arr[i_idx][j_idx +1 ]
        right_arr[i_idx][j_idx + 1] = tmp
        
        for i in range(3):
            for j in range(3):
                right_side[i][j] = right_arr[i][j]
                
        global key
        global parent
        
        upload = False
        find( key )# parent 에다가 조상님들 싹다 넣기.
         
        if right_side not in parent:
            upload = True
                        
        parent = []      
        if( upload == True):
           
            key +=1 #딕셔너리 키값 1증가.
        
            Dic[key] = right_side#딕셔너리에 추가.
        
            G.add_edge(key_of_parent,key)
        
    if 0<=( i_idx + 1) <=2 and 0<=( j_idx ) <= 2:#공백 블록이 아랫칸으로 이동 가능하다는 의미.
        tmp = down_arr[i_idx][j_idx]
     
        down_arr[i_idx][j_idx] = down_arr[i_idx+1][j_idx]
        down_arr[i_idx+1][j_idx] = tmp
        
        for i in range(3):
            for j in range(3):
                down_side[i][j] = down_arr[i][j]
                
        global key
        global parent
        
        upload = False
        find( key )# parent 에다가 조상님들 싹다 넣기.
        
      
        if down_side not in parent:
             upload = True
             
        parent = []      
        if( upload == True):
        
            key +=1 #딕셔너리 키값 1증가.
        
            Dic[key] = down_side#딕셔너리에 추가.
        
            G.add_edge(key_of_parent,key)
    
        
    
 ############################################################################################3       
        
                
    
    

  
 #2차원 배열에다가 번호 할당     
G.add_node(1)# 그 번호를 그래프에 저장( 즉, 2차원 배열 을 저장)
# 노드 추가햇을때, 해당 노드( 2차원 배열) 에서 자식으로 생성시킬수 있는 노드들 검사후, add_edge 로 추가시켜준다.
# 추가시키고 나서 bfs 로 검사해야 하나???

#G.add_edge("a","b")




i=1

ee = False
while( True ):
 
    child_check(Dic[i])
 
    i += 1
    if( i%1000 == 0 ):
        ee = bfs(G,1)
      
    if( ee ):
        print "진입성공"
        
        break


   
print "################################################################################"



print pathh
for i in pathh:
    show(Dic[i])
    print "========"      
#    print str(i)+"\n"

#bfs( G, 1)
print "################################################################################"

"""
#print bfs( G, "1")
net.draw(G)
plt.savefig("ddd.png")
plt.show()
"""