
class Solution:
    def subsets(self, nums) :
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
    # def subsets(self, nums) :
    #     res=[[]]
    #     for i in nums:
    #         res=res+[n+[i] for n in res]
    #     return res
    #  def subsetsWithDup(self, nums):
    #     res=[[]]
    #     pre=None;
    #     for i in nums:
    #         if (i==pre):
    #             continue
    #         else:
    #             res=res+[n+[i] for n in res]
    #             pre=i
    #     return res

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            count=0;
            for c in s:
                if c == "(": count+=1;
                elif c ==")":count-=1;
                if count<0: return False;
            return count==0
        level={s}
        while True:
            valid=list(filter(isValid,level));
            if valid: return valid
            next_level=set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":
                        next_level.add(item[:i]+item[i+1:])
            level=next_level

        def removeInvalidParentheses(self, s:str) -> List[str]:
            def isValid(s:str)->bool:
                cnt = 0
                for c in s:
                    if c == "(": cnt += 1
                    elif c == ")": cnt -= 1
                    if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
                return cnt == 0

        # BFS
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid # 如果当前valid是非空的，说明已经有合法的产生了
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":                     # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i]+item[i+1:])
            level = next_level
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 如果只有数字，直接返回
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res
    def search(self, nums, target):
        left ,right =0,len(nums)-1;
        while(left<right):
            mid=left+(right-left)/2
            if(nums[mid]==target):
                return mid
            if(nums[mid]>target):
                right=mid-1
            if(nums[mid]<target):
                left=mid+1
        
        return -1
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while(l<=r):
            mid =l+(r-l)/2
            if(nums[mid]==target):
                return mid
            if(nums[mid]<target):
                l=mid+1
            if(nums[mid]>target):
                r=mid-1
            
        return l
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == "__main__":
    nums = [1,2,3]
    s=Solution()
    s.subsets(nums)
    a=1
    b=2
    print(a,b)
