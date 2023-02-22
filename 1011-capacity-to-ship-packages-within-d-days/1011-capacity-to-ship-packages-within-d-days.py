class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # initialize the minimum and maximum possible weight capacities
        min_capacity = max(weights)
        max_capacity = sum(weights)

        # perform binary search to find the minimum weight capacity
        while min_capacity < max_capacity:
            mid_capacity = (min_capacity + max_capacity) // 2
            day_count = 1
            total_weight = 0

            # calculate the number of days required to load all packages
            for weight in weights:
                if total_weight + weight > mid_capacity:
                    day_count += 1
                    total_weight = 0
                total_weight += weight

            # adjust the weight capacity range based on the number of days
            if day_count <= days:
                max_capacity = mid_capacity
            else:
                min_capacity = mid_capacity + 1

        return min_capacity