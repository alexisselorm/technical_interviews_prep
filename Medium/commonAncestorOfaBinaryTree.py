
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root,p,q)
    
    
    def dfs(self,node,p,q):
        if node is None:
            return None
        
        if node.val == p.val or node.val == q.val:
            return node
        
        left_subtree = self.dfs(node.left,p,q)
        right_subtree = self.dfs(node.right,p,q)
        
        if left_subtree is None:
            return right_subtree
        
        if right_subtree is None:
            return left_subtree
        
        return node