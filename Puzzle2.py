# -*- coding: utf-8 -*-


start = [3,7,0,1,6,2,5,4,8]
goal = [1,2,3,8,0,4,7,6,5]

# Define the Node class ( For contain shape , parent , depth info )
class Node:
    def __init__(self, shape , parent , depth ):
        self.shape = shape
        self.parent = parent
        self.depth = depth
        
    def rt_depth( self ):
        return self.depth
#node_make acts as making new Node.
def node_make( shape, parent, depth ):
    return Node( shape , parent , depth )

#show acts as just making a puzzle shape.
def show( arr ):
    print arr[0],arr[1],arr[2]
    print arr[3],arr[4],arr[5]
    print arr[6],arr[7],arr[8]
   
#Below 4 function acts like that
#find the idx of blank,and change shape if the blank can move. 
def upside( arr ):
    up = arr[:]
    idx = arr.index(0)
    if idx not in [0,1,2]:
        tmp = up[ idx - 3 ]
        up[idx-3] = up[idx]
        up[idx] = tmp
        return up
    else:
        return
        
def downside( arr ):
    down = arr[:]
    idx = arr.index(0)
    if idx not in [6,7,8]:
        tmp = down[ idx + 3 ]
        down[idx+3] = down[idx]
        down[idx] = tmp
        return down
    else:
        return
        
def leftside( arr ):
    left = arr[:]
    idx = arr.index(0)
    if idx not in [0,3,6]:
        tmp = left[ idx - 1 ]
        left[idx-1] = left[idx]
        left[idx] = tmp
        return left
    else:
        return
        
def rightside( arr ):
    right = arr[:]
    idx = arr.index(0)
    if idx not in [2,5,8]:
        tmp = right[ idx+1 ]
        right[idx+1] = right[idx]
        right[idx] = tmp
        return right
    else:
        return
#this function acts for relation between parent and child.     
def find_child ( node , nodes ):
    child_lst = []
    idx = node.shape.index(0)
    if idx not in [2,5,8]:
        child_lst.append( node_make(  rightside(node.shape) , node , node.depth+1 ))
    if idx not in [0,3,6]:
        child_lst.append( node_make(  leftside(node.shape) , node , node.depth+1 ))
    if idx not in [0,1,2]:
        child_lst.append( node_make(  upside(node.shape) , node , node.depth+1 ))
    if idx not in [6,7,8]:
        child_lst.append( node_make(  downside(node.shape) , node , node.depth+1 ))
    return child_lst

#bfs function check every path for finding goal shape.
def bfs ( start , goal ):
    #make a node list for containing every movements
    nodes = []
    tmp = []# for containing new nodes
    tmp_shape=[]#for containing shapes of new nodes
    same_depth =[]
    level = 0 # This is depth of tree
    # input the start node into list
    nodes.append( node_make( start , None , 0 ))
    while(1):
        #pop the latest node for checking.
        ########node = tmp.pop(0)#추가된것들중에서  검사해버림???
        
        
        for Node in nodes:
            
            if( Node.rt_depth == level ):
                tmp_shape.append( Node.shape )
                same_depth.append( Node )
###############################################################       
        if goal in tmp_shape:
            for i in range( len(tmp_shape) ):
                if( tmp_shape[i] == goal ):
                    stop = i
            for i in range( len(tmp) ):
                if( tmp[i].shape == tmp_shape[ stop ]  ):
                    node = tmp[i]
                    #######if node.shape == goal:
            #make a list for containing the route.
            path = []
            #tmp is for moving to ancestor
            tmp = node
            while(1):
                #insert self into path
                path.insert(0,tmp.shape)
                # tmp.depth == 0 means root.
                if tmp.depth == 0:
                    break
                #move to the ancestor
                tmp = tmp.parent
            return path
#########################################################################
        # if node is not equal with the goal , then find each node's child.
        for node in same_depth:
            tmp = find_child( node, nodes )
        #nodes.extend( tmp )
            nodes.append(tmp)
            
        level+=1
        
        
        
        # depth 같은 애들끼리 일괄 검사 후, 그 자식depth 라인 일괄검사 => 로테잇ㄴ
result =  bfs( start , goal )
for i in result:
    show(i)
    print "-----"
  