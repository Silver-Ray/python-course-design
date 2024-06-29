vector_1=[0,1,2,3,4,5,6]
vector_2=[7,8,9,10,11,12,13]

def distance_v1_v2(vector1,vector2):

    if type=='欧式距离':
    result= 0
    for i in range(7):
        result=result+(vector1[i]-vector2[i])**2
    result=math.sqrt(result)
        return result


result=distance_v1_v2(vector_1,vector_2)
