class SortAlgos:

    # divide and conquer
    # make 2 lists based on the mid point : left and right
    # recursively break the left and right till they become single element list
    # merge the individuals into list
    # create the final merged list
    # merge 2 sorted lists with may be unequal lengths
    # questions :
    # does input have duplicate elements ?
    # what if list length is zero ?
    # does input have negative elements ?
    # can i use any built in python functions ? this question is asked when actually in that scenario


    def bucket_sort(self, l):
        pass

    def radix_sort(self, l):
        pass

    def selection_sort(self, l):
        for i in range(len(l)):
            min_ind = i
            for j in range(i + 1, len(l)):
                if l[min_ind] > l[j]:
                    min_ind = j
            if i != min_ind:
                l[i], l[min_ind] = l[min_ind], l[i]
        return l

    def quick_sort(self, l):
        if len(l) <= 1:
            return l

        pivot = l.pop()
        left = []
        right = []
        for item in l:
            if item > pivot:
                right.append(item)
            else:
                left.append(item)
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)


    def bubble_sort(self, l):
        for i in range(len(l)):
            for j in range(len(l) - i - 1):
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]
        return l

    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = self.merge_sort(lst[:mid])
        right = self.merge_sort(lst[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        left_index = 0
        right_index = 0
        merged_list = []
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[left_index]:
                merged_list.append(left[left_index])
                left_index += 1
            else:
                merged_list.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged_list.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged_list.append(right[right_index])
            right_index += 1

        return merged_list


l = [2,3,6,8,4,5,0]
sortalgo = SortAlgos()
l1 = [3]
l2 = [1]
# print(sortalgo.merge_sort(l))
# print(sortalgo.merge(l1, l2))
# print(sortalgo.bubble_sort(l))
# print(sortalgo.quick_sort(l))
print(sortalgo.selection_sort(l))



