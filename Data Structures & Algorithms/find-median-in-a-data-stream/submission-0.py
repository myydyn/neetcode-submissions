class MedianFinder:

    def __init__(self):
        # self.small: heap chứa nửa nhỏ của dãy (mô phỏng max-heap bằng cách lưu giá trị âm)
        # self.large: heap chứa nửa lớn của dãy (min-heap bình thường)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Nếu heap large không rỗng và num lớn hơn phần tử nhỏ nhất của large
        # → số này thuộc nửa lớn, đẩy vào large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # Ngược lại, đẩy vào small (nửa nhỏ), lưu dưới dạng âm để mô phỏng max-heap
            heapq.heappush(self.small, -num)

        # Cân bằng kích thước 2 heap sao cho chênh lệch không quá 1
        if len(self.small) > len(self.large) + 1:
            # Nếu small có nhiều hơn 1 phần tử → chuyển phần tử lớn nhất (tức là -min) sang large
            val = -heapq.heappop(self.small)   # Lấy phần tử lớn nhất của small
            heapq.heappush(self.large, val)    # Đưa sang large
        if len(self.large) > len(self.small) + 1:
            # Nếu large nhiều hơn 1 phần tử → chuyển phần tử nhỏ nhất sang small
            val = heapq.heappop(self.large)    # Lấy phần tử nhỏ nhất của large
            heapq.heappush(self.small, -val)   # Đưa sang small dưới dạng âm

    def findMedian(self) -> float:
        # Nếu small có nhiều phần tử hơn → median là phần tử lớn nhất của small
        if len(self.small) > len(self.large):
            return -self.small[0]  # Đảo dấu để trả lại giá trị thật
        # Nếu large có nhiều phần tử hơn → median là phần tử nhỏ nhất của large
        elif len(self.large) > len(self.small):
            return self.large[0]
        # Nếu hai heap bằng nhau → median là trung bình của hai phần tử đỉnh
        return (-self.small[0] + self.large[0]) / 2.0
        