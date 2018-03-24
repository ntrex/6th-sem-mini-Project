import PIL
from PIL import Image
xx=[2,3,4,5,7]
for X in xx:
    thefile = open('features_'+str(X)+'.txt', 'w')
    print(X)
    try:
        for k in range(1,742,1):
            try:
                img = Image.open('Last_'+str(X)+'/'+str(X)+'_('+str(k)+').jpeg')
            except Exception as e:
                print(e)
                continue
            w,h=img.size
            print(w,h)
            import numpy as np
            arr = np.array(img)

            arr[arr<200]=0;
            arr[arr>=200]=1;
            a=[]
            '''for i in range(0,50):
                for j in range(0,50):
                    #arr[i][j]/=255;
                    print(arr[i][j],end=' ')
                print()
            '''
            for i in range(0,50):
                f=0
                for j in range(0,50):
                    if arr[i][j] == 0:
                        a.append(j)
                        f=1
                        break
                if f==0:
                    a.append(-1)

            for j in range(0, 50):
                f = 0
                for i in range(49, -1,-1):
                    if arr[i][j] == 0:
                        a.append(i)
                        f = 1
                        break
                if f == 0:
                    a.append(-1)
            for i in range(49, -1,-1):
                f = 0
                for j in range(49,-1,-1):
                    if arr[i][j] == 0:
                        a.append(j)
                        f = 1
                        break
                if f == 0:
                    a.append(-1)
            for j in range(49, -1,-1):
                f = 0
                for i in range(0, 50):
                    if arr[i][j] == 0:
                        a.append(i)
                        f = 1
                        break
                if f == 0:
                    a.append(-1)

            for i in range(0,50):
                max = 0
                count=0
                for j in range(0,50):
                    if j==0 and arr[i][j] == 0:
                        count = count+1;
                        if(count>max):
                            max=count
                        continue;
                    if arr[i][j] == 0 and arr[i][j-1] == 0 :
                        count = count+1
                        if (count > max):
                            max = count
                    if arr[i][j] == 0 and arr[i][j-1] == 1 :
                        count = 1
                        if (count > max):
                            max = count
                a.append(max)

            for i in range(0,50):
                max = 0
                count=0
                for j in range(0,50):
                    if j==0 and arr[j][i] == 0:
                        count = count+1;
                        if(count>max):
                            max=count
                        continue;
                    if arr[j][i] == 0 and arr[j-1][i] == 0 :
                        count = count+1
                        if (count > max):
                            max = count
                    if arr[j][i] == 0 and arr[j-1][i] == 1 :
                        count = 1
                        if (count > max):
                            max = count
                a.append(max)

            for k in range(0,49,1):
                i=k
                j=0
                max=0
                count=0
                while(i<50):
                    if j==0 and arr[i][j] == 0:
                        count = count+1;
                        if(count>max):
                            max=count
                        continue;
                    if arr[i][j] == 0 and arr[i-1][j-1] == 0 :
                        count = count+1
                        if (count > max):
                            max = count
                    if arr[i][j] == 0 and arr[i-1][j-1] == 1 :
                        count = 1
                        if (count > max):
                            max = count
                    i = i+1
                    j = j+1
                a.append(max)

            for k in range(1,49,1):
                j=k
                i=0
                max=0
                count=0
                while(j<50):
                    if i==0 and arr[i][j] == 0:
                        count = count+1;
                        if(count>max):
                            max=count
                        continue;
                    if arr[i][j] == 0 and arr[i-1][j-1] == 0 :
                        count = count+1
                        if (count > max):
                            max = count
                    if arr[i][j] == 0 and arr[i-1][j-1] == 1 :
                        count = 1
                        if (count > max):
                            max = count
                    i = i+1
                    j = j+1
                a.append(max)

            for k in range(0,49,1):
                i=k
                j=49
                max=0
                count=0
                while(i<50):
                    if j==49 and arr[i][j] == 0:
                        count = count+1;
                        if(count>max):
                            max=count
                        continue;
                    if arr[i][j] == 0 and arr[i-1][j+1] == 0 :
                        count = count+1
                        if (count > max):
                            max = count
                    if arr[i][j] == 0 and arr[i-1][j+1] == 1 :
                        count = 1
                        if (count > max):
                            max = count
                    i = i+1
                    j = j-1
                a.append(max)
            for k in range(48,0,-1):
                j=k
                i=0
                max=0
                count=0
                while(j>=0):
                    if i==0 and arr[i][j] == 0:
                        count = count+1;
                        if(count>max):
                            max=count
                        continue;
                    if arr[i][j] == 0 and arr[i-1][j+1] == 0 :
                        count = count+1
                        if (count > max):
                            max = count
                    if arr[i][j] == 0 and arr[i-1][j+1] == 1 :
                        count = 1
                        if (count > max):
                            max = count
                    i = i+1
                    j = j-1
                a.append(max)

            thefile.write(",".join(map(lambda x: str(x), a)))
            thefile.write(","+str(X)+"\n");
            #print(len(a))
        thefile.close()
    except Exception as e:
        print(e)
