class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width =1
        curr_level = [(root , 1)]
        while curr_level != []:
            next_level = []
            for nodes,pos in curr_level:
                if nodes.left:
                    next_level.append((nodes.left,pos*2))
                if nodes.right:
                    next_level.append((nodes.right, pos*2+1))
            if next_level !=[]:
                max_width = max(max_width,next_level[-1][1] - next_level[0][1] +1)
            curr_level = next_level
        return max_width