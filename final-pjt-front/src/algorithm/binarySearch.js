const binarySearch = (list, target) => {
  let left = 0
  let right = list.length - 1
  let mid

  while (left <= right) {
    mid = Math.floor((left + right) / 2)

    if (list[mid] === target) {
      return mid
    }

    if (list[mid] > target) {
      right = mid - 1
    } else {
      left = mid + 1
    }
  }

  return [left, mid, right]
}

console.log(binarySearch([1, 2, 3, 4, 5, 6, 8, 9, 10], 7))

// export default binarySearch
