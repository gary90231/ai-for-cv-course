

def filter(x, y, img, kernel, step):
    sum_s=[]

    for k in range(-int(step/2), int(step/2)):
        for j in range(-int(step/2), int(step/2)):
            sum_s.append(img[x+k][y+m]*kernel[k][j])
    sum_s.sort()
    return sum_s[int(step*step/2)+1]

def medianBlur(img, kernel, padding_way):
        step = 1
        padd_size = 1
        im = []
        w = img.shape[0]
        h = img.shape[1]
        m = kernel.shape[0]
        n = kernel.shape[1]
        if (cmp(padding_way, 'REPLICA') == 0)
            padd_flag = 1
        else if (cmp((padding_way, 'ZERO') == 0)
            padd_flag = 2
        else
            print("Error padding_way input")
            return
        if (padd_flag == 1)
            for i in range(0, w+size*2):
                for j in rnage(0, h+size*2):
                    if ((i < size)&&(j<size))
                        im[i][j] = img[i-size>=0][j-size>=0]
                    else if ((i>w+size) && (j>h+size))
                        im[i][j] = img[i-size<w][j-size<h]
        else
            for i in range(0, w+size*2)
                for j in rnage(0, h+size*2)
                    if (((i < size)&&(j<size)) || ((i>w+size) && (j>h+size)))
                       im[i][j] = 0

        for i in range(int(step/2), w-int(step/2)):
            for j in range(int(step/2), h-int(step/2)):
                result[i][j] = filter(i, j, im, kernel, step)
            return result
	
