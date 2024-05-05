def count_even_odd_pairs(A):
    even_count = 0
    odd_between_count = 0
    pair_count = 0

    for i in range(len(A)):
        if A[i] % 2 == 0:  # Nếu A[i] là số chẵn
            even_count += 1
            odd_between_count = 0  # Reset đếm số lẻ khi gặp số chẵn mới
        else:
            odd_between_count += even_count  # Cập nhật số lẻ nằm giữa các số chẵn

        for j in range(i+1, len(A)):
            if A[j] % 2 == 0 and A[i] > A[j]:
                pair_count += odd_between_count  # Đếm cặp thỏa mãn điều kiện

    return pair_count

# Ví dụ sử dụng hàm:
n = int(input())
A = arr
print(count_even_odd_pairs(A))
