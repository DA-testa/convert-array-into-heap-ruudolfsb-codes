def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        sift_down(i, data, swaps)
    return swaps

def sift_down(i, data, swaps):
    min = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(data) and data[left] < data[min]:
        min = left
    if right < len(data) and data[right] < data[min]:
        min = right

    if i != min:
        data[i], data[min] = data[min], data[i]
        swaps.append((i, min))
        sift_down(min, data, swaps)

def main():
    input_type = input()
    if "I" in input_type:
        nave = int(input())
        data = list(map(int, input().split()))
    elif "F" in input_type:
        filename = input()
        if "a" not in filename:
            with open("./tests/"+filename, mode='r') as fails:
                nave = int(fails.readline())
                data = list(map(int, fails.readline().split()))
    else:
        print("error")
        return
    
    assert len(data) == nave
    
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()