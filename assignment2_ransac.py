
def ransacMatching(A, B):
    d = 100
    iterations = 0
    while (iterations < k):
        inliers = A1,A2,A3,A4 #random select 4 points in A
        model = (A1-Bx,A2-By,A3-Bz,A4-Bq) # A sepecial model correspoding from A to B 
        set = model
        for Ai in A but not in inliers:
            if according to the below special model Ai-Bj and error < t
                put Ai into set
        if (numbers of set > d):
            if (this_model_error < best_model_error):
                best_model = model
				best_model_error = this_model_error
		iterations++
	return best_model, best_model_error