# O(n)
# using DFS

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        # image looks like this:
        #
        #          c1 c2 c3 c4
        # image: [[1, 1, 1, 1], r1
        #         [1, 1, 0, 0], r2
        #         [1, 1, 1, 0], r3
        #         [1, 1, 0, 0]] r4

        # sr sc is the starting pixel

        R, C = len(image), len(image[0])
        color = image[sr][sc]
        # if new colour is same are old colour then return image as is
        if color == newColor: return image

        # if not then go directions sis!
        def dfs(r, c):
            #but only if the colour of that image is same as OG colour
            if image[r][c] == color:
                image[r][c] = newColor # then change its colour
                if r >= 1: dfs(r-1, c) # check for bounds and then do UP!
                if r+1 < R: dfs(r+1, c) # go DOWN!
                if c >= 1: dfs(r, c-1) # go LEFT!
                if c+1 < C: dfs(r, c+1) # go RIGHT

        dfs(sr, sc)
        return image